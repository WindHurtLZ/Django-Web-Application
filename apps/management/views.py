import json
import logging
import re

import requests
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from apps.management.forms import DeviceForm
from apps.management.models import Device
from apps.management.onem2m_service import logger, generate_request_identifier
from apps.widgets.models import DeviceData
from core import settings

# Create your views here.

@login_required(login_url="/login/")
def index(request):

    form = DeviceForm()
    user_devices = Device.objects.filter(owner=request.user)
    context = {'devices': user_devices, 'form': form}

    return render(request, 'management/index.html', context)

@login_required(login_url="/login/")
def device(request):

    form = DeviceForm()
    user_devices = Device.objects.filter(owner=request.user)
    context = {
        'devices': user_devices,
        'form': form,
        'ONE_M2M_CSE_URL': settings.ONE_M2M_CSE_URL,
    }

    return render(request, 'management/device.html', context)

@login_required(login_url="/login/")
def add_device(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            new_device = form.save(commit=False)
            new_device.owner = request.user  # Set the owner to the current user
            new_device.ae_rn = form.cleaned_data['name'].replace(" ","") + "-AE"
            new_device.save()
            return redirect('device')  # Redirect to the device list after saving
    else:
        form = DeviceForm()

    return render(request, 'management/device.html', {'form': form})

@login_required(login_url="/login/")
def delete_device(request):
    if request.method == 'POST':
        device_ids = request.POST.get('device_ids')
        if device_ids:
            device_ids_list = device_ids.split(',')
            devices_to_delete = Device.objects.filter(id__in=device_ids_list, owner=request.user)
            devices_to_delete.delete()
    return redirect('device')


@csrf_exempt
def receive_notification(request):

    if request.method == 'GET':
        return JsonResponse({"status": "success", "message": "Verification successful"}, status=200)

    if request.method == 'POST':
        try:

            content_type = request.headers.get('Content-Type', '')
            if 'application/json' in content_type or 'application/vnd.onem2m-res+json' in content_type:
                payload = json.loads(request.body)
            else:
                logger.error(f"Unsupported Content-Type: {content_type}")
                return JsonResponse({"status": "error", "message": "Unsupported Content-Type"}, status=415)

            logger.debug(f"Received notification: {payload}")

            if payload.get('m2m:sgn', {}).get('vrq', False):
                logger.info("Received verification request. Responding with 200 OK.")

                response = HttpResponse(content_type="application/json", status=200)
                response['X-M2M-RSC'] = '2000'  # Success response code for oneM2M
                response['X-M2M-RI'] = request.headers.get('X-M2M-RI', '')
                return response

            logger.info("Processing actual data notification...")

            notification = payload.get('m2m:sgn', {})
            nev = notification.get('nev', {})
            rep = nev.get('rep', {})
            cin = rep.get('m2m:cin', {})
            rn = cin.get('rn', {})

            query_url = f"{settings.ONE_M2M_CSE_URL}?fu=1&ty=4&rn={rn}"
            headers = {
                "X-M2M-Origin": "CAdmin",
                "X-M2M-RI": generate_request_identifier(),
                "X-M2M-RVI": "3",
                "Accept": "application/json"
            }
            response = requests.get(query_url, headers=headers)
            if response.status_code == 200:
                uril_list = response.json().get("m2m:uril", [])
                if uril_list:

                    full_path = uril_list[0]
                    ae_rn = full_path.split('/')[1]  # extract AE resource name

                    try:
                        device = Device.objects.get(ae_rn=ae_rn)
                    except Device.DoesNotExist:
                        logger.error(f"No device found for AE Resource Name: {ae_rn}")
                        return JsonResponse({'status': 'error', 'message': 'Device not found'}, status=404)

                    con_str = cin.get('con')
                    try:
                        con = json.loads(con_str)
                    except (json.JSONDecodeError, TypeError):
                        logger.error(f"Invalid JSON content in `con`: {con_str}")
                        return JsonResponse({"status": "error", "message": "Invalid JSON content in `con`"}, status=400)

                    temperature = con.get('temperature')
                    speed = con.get('speed')
                    latitude = con.get('latitude')
                    longitude = con.get('longitude')

                    DeviceData.objects.create(
                        device=device,
                        temperature=temperature if temperature is not None else None,
                        speed=speed if speed is not None else None,
                        latitude=latitude if latitude is not None else None,
                        longitude=longitude if longitude is not None else None
                    )

                    logger.info(f"DataInstance created for device '{device.name}': {con}")
                    return JsonResponse({"status": "success"}, status=200)
                else:
                    logger.error("No uril returned from CSE query")
                    return JsonResponse({"status": "error", "message": "No uril found"}, status=404)
            else:
                logger.error(f"Failed to query CSE for uril: {response.status_code}, {response.text}")
                return JsonResponse({"status": "error", "message": "Failed to query CSE"}, status=500)

        except json.JSONDecodeError:
            logger.error("Invalid JSON received")
            return JsonResponse({"status": "error", "message": "Invalid JSON"}, status=400)

        except Exception as e:
            logger.exception(f"Error processing notification: {e}")
            return JsonResponse({"status": "error", "message": str(e)}, status=500)