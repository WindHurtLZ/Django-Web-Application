from django.urls import include, path

from apps.widgets import views

urlpatterns = [

    path('map/', views.device_map, name='map'),

]