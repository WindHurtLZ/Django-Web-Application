from django.urls import include, path

from apps.widgets import views

urlpatterns = [
    path('map/', views.device_map, name='map'),
    path('logs/', views.device_logs, name='logs'),
    path('device-path/<int:device_id>/', views.device_path, name='device_path'),
    path('device-data/', views.device_data, name='device_data'),

]