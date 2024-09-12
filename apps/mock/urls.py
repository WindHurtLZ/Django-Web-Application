from django.urls import include, path

from apps.mock import views

urlpatterns = [

    path('simulate-device-movement/', views.simulate_device_movement, name='simulate_device_movement'),

]