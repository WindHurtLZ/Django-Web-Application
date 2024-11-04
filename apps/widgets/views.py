from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from apps.management.models import Device
from apps.management.onem2m_service import logger
from apps.widgets.models import DeviceData, MeshConnectivity
from core.decorators import superuser_required

"""
MAP Widget
"""
@login_required(login_url="/login/")
@superuser_required
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


"""
LOG Widget
"""
@login_required(login_url="/login/")
@superuser_required
def device_logs(request):
    return render(request, 'widgets/logs.html')

"""
MESH Widget
"""
@login_required(login_url="/login/")
@superuser_required
def device_mesh(request):
    return render(request, 'widgets/mesh_tree.html')

"""
Data API
"""
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
            latest_data = device.data.last()  # Get the latest path

            latest_ride = device.rides.filter(end_time__isnull=True).order_by('-start_time').first()

            if latest_data:
                # Calculate the duration of the current ride if active
                if latest_ride and latest_ride.start_time and not latest_ride.end_time:
                    ride_duration_seconds = (timezone.now() - latest_ride.start_time).total_seconds()
                else:
                    ride_duration_seconds = None

                data = {
                    'device_name': device.name,
                    'current_rider': device.user.username if device.user else 'None',
                    'ride_duration': f"{int(ride_duration_seconds // 3600):02}:{int((ride_duration_seconds % 3600) // 60):02}:{int(ride_duration_seconds % 60):02}" if ride_duration_seconds is not None else 'None',
                    'temperature': latest_data.temperature,
                    'speed': latest_data.speed,
                    'latitude': latest_data.latitude,
                    'longitude': latest_data.longitude,
                }
                data_list.append(data)

        return JsonResponse({'status': 'success', 'data': data_list}, status=200)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

def mesh_network_data(request):
    try:
        devices = Device.objects.all()
        mesh_connections = MeshConnectivity.objects.all()

        nodes = []
        links = []

        device_map = {device.hardware_id: device.name for device in devices}

        # Add all device as Node
        for device in devices:
            nodes.append({
                'id': device.hardware_id,
                'name': device.name
            })

        # Connect each node if data have
        for connection in mesh_connections:
            if connection.parent_id:
                links.append({
                    'source': connection.device.hardware_id,
                    'target': connection.parent_id,
                    'rssi': connection.rssi
                })

        return JsonResponse({'nodes': nodes, 'links': links}, status=200)

    except Exception as e:
        logger.error(f"Error in mesh_network_api: {e}")
        return JsonResponse({'error': 'Internal Server Error'}, status=500)