from django.urls import include, path

from apps.home import views

urlpatterns = [

    path('', views.index, name='home'),
    path('device/', views.device, name='device'),
    path('add_device/', views.add_device, name='add_device'),
    path('delete_device/', views.delete_device, name='delete_device'),
    
]