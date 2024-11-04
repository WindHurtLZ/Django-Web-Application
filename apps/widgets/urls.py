from django.urls import include, path

from apps.widgets import views

urlpatterns = [
    path('map/', views.device_map, name='map'),
    path('logs/', views.device_logs, name='logs'),
    path('mesh/', views.device_mesh, name='mesh'),
    path('device-path/<int:device_id>/', views.device_path, name='device_path'),
    path('device-data/', views.device_data, name='device_data'),
    path('mesh-network-data/', views.mesh_network_data, name='mesh_network_data'),

]