import json

from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from apps.management.models import Device
from apps.management.onem2m_service import update_lock_module


# Create your views here.
@login_required(login_url="/login/")
def home(request):
    return render(request, 'home/home.html')

@login_required(login_url="/login/")
def ride1_view(request):
    return render(request, 'home/ride-1.html')

def ride2_view(request):
    if not request.session.get('bike_number'):
        return redirect('home')
    return render(request, 'home/ride-2.html')

def ride3_view(request):
    bike_id = request.session.get('bike_number')

    if not bike_id:
        return redirect('home')

    # Send PUT to update Unlock resource here
    device = get_object_or_404(Device, hardware_id=bike_id)
    ae_rn = device.ae_rn
    originator = f"C{device.type}_{str(device.ae_id)[:8]}"
    update_lock_module(ae_rn, originator, status=False)

    request.session.pop('bike_number', None)
    return render(request, 'home/ride-3.html')

def validate_bike_number(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        bike_number = data.get('bike_number')

        try:
            device = Device.objects.get(hardware_id=bike_number, user=None)
            device.user = request.user
            device.save()

            # Session flag
            request.session['bike_number'] = bike_number

            return JsonResponse({'valid': True})
        except Device.DoesNotExist:
            return JsonResponse({'valid': False})

    return JsonResponse({'valid': False})

