from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

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

@login_required(login_url="/login/")
def device_logs(request):
    return render(request, 'widgets/logs.html')

def device_path(request, device_id):
    paths = Map.objects.filter(device_id=device_id).order_by('timestamp')
    # if paths exist，return latest position
    if paths.exists():
        latest_position = {
            'latitude': paths.last().latitude,
            'longitude': paths.last().longitude
        }
    else:
        latest_position = {'latitude': None, 'longitude': None}

    # check full path parameter
    if 'full_path' in request.GET:
        path_data = [{'latitude': path.latitude, 'longitude': path.longitude} for path in paths]
        return JsonResponse({'path': path_data, 'latest_position': latest_position}, safe=False)

    # return latest position default
    return JsonResponse(latest_position, safe=False)

@csrf_exempt
def device_data(request):
    if request.method == 'GET':
        devices = Device.objects.prefetch_related('paths')  # Prefetch related paths

        data_list = []
        for device in devices:
            latest_path = device.paths.last()  # Get the latest path
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