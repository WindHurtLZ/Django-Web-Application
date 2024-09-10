from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from apps.home.models import Device
from apps.widgets.models import Map


# Create your views here.
@login_required(login_url="/login/")
def device_map(request):

    devices = Device.objects.all().prefetch_related('paths')

    # QuerySet to JSON
    devices_data = []
    for device in devices:
        device_info = {
            'id': device.id,
            'name': device.name,
            'latitude': device.paths.last().latitude if device.paths.exists() else 'null',
            'longitude': device.paths.last().longitude if device.paths.exists() else 'null',
            'paths': [{'latitude': path.latitude, 'longitude': path.longitude} for path in device.paths.all()]
        }
        devices_data.append(device_info)

    context = {'devices': devices_data}
    return render(request, 'widgets/map.html', context)


def device_path(request, device_id):
    paths = Map.objects.filter(device_id=device_id).order_by('timestamp')
    path_data = [{'latitude': path.latitude, 'longitude': path.longitude} for path in paths]
    return JsonResponse(path_data, safe=False)