from django.urls import include, path

from apps.home import views

urlpatterns = [

    path('home/', views.home, name='home'),
    path('ride-1/', views.ride1_view, name='ride-1'),
    path('ride-2/', views.ride2_view, name='ride-2'),
    path('ride-3/', views.ride3_view, name='ride-3'),
    path('ride-4/', views.ride4_view, name='ride-4'),

    path('validate-bike-number/', views.validate_bike_number, name='validate-bike-number'),
    path('get-user-ride-info/', views.get_user_ride_info, name='get-user-ride-info'),
    path('end-ride/', views.end_ride, name='end-ride'),
]