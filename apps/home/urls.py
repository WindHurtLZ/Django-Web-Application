from django.urls import include, path

from apps.home import views

urlpatterns = [

    path('', views.index, name='home'),
    path('device/', views.device, name='device'),
    
]