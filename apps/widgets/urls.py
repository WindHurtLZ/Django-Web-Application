from django.urls import include, path

from apps.widgets import views

urlpatterns = [

    path('device-path/<int:device_id>/', views.device_path, name='device_path'),
    path('map/', views.device_map, name='map'),

]