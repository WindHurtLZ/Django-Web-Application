from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from apps.home.models import Device
from apps.widgets.models import DeviceData


# Create your views here.
@login_required(login_url="/login/")
def device_map(request):

    devices = Device.objects.all().prefetch_related('data')

    # QuerySet to JSON
    devices_data = []
    for device in devices:
        device_info = {
            'id': device.id,
            'name': device.name,
            'latitude': device.data.last().latitude if device.data.exists() else 'null',
            'longitude': device.data.last().longitude if device.data.exists() else 'null',
            'paths': [{'latitude': path.latitude, 'longitude': path.longitude} for path in device.data.all()]
        }
        devices_data.append(device_info)

    context = {'devices': devices_data}
    return render(request, 'widgets/map.html', context)

@login_required(login_url="/login/")
def device_logs(request):
    return render(request, 'widgets/logs.html')

def device_path(request, device_id):
    data = DeviceData.objects.filter(device_id=device_id).order_by('timestamp')
    # if data exist，return latest position
    if data.exists():
        latest_position = {
            'latitude': data.last().latitude,
            'longitude': data.last().longitude
        }
    else:
        latest_position = {'latitude': None, 'longitude': None}

    # check full path parameter
    if 'full_path' in request.GET:
        path_data = [{'latitude': path.latitude, 'longitude': path.longitude} for path in data]
        return JsonResponse({'path': path_data, 'latest_position': latest_position}, safe=False)

    # return latest position default
    return JsonResponse(latest_position, safe=False)

@csrf_exempt
def device_data(request):
    if request.method == 'GET':
        devices = Device.objects.prefetch_related('data')  # Prefetch related data

        data_list = []
        for device in devices:
            latest_path = device.data.last()  # Get the latest path
            if latest_path:
                data = {
                    'device_name': device.name,
                    'temperature': latest_path.temperature,
                    'speed': latest_path.speed,
                    'latitude': latest_path.latitude,
                    'longitude': latest_path.longitude,
                }
                data_list.append(data)

        return JsonResponse({'status': 'success', 'data': data_list}, status=200)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)