from django.urls import include, path

from apps.widgets import views

urlpatterns = [
    path('map/', views.device_map, name='map'),
    path('logs/', views.device_logs, name='logs'),
    path('mesh/', views.device_mesh, name='mesh'),
    path('device-path/<int:device_id>/', views.device_path, name='device_path'),
    path('device-data/', views.device_data, name='device_data'),
    path('mesh-network-data/', views.mesh_network_data, name='mesh_network_data'),
    path('device_speed_data/<int:device_id>/', views.device_speed_data, name='device_speed_data'),
    path('device_latest_speed/<int:device_id>/', views.device_latest_speed, name='device_latest_speed'),

]