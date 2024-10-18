from django.urls import include, path

from apps.management import views
from apps.management.views import receive_notification

urlpatterns = [

    path('', views.index, name='management'),
    path('device/', views.device, name='device'),
    path('add_device/', views.add_device, name='add_device'),
    path('delete_device/', views.delete_device, name='delete_device'),

    # Important Not, do not add / behind the notifications, OneM2M will ignore the last / when it sends any info
    path('notifications', views.receive_notification, name='receive_notification'),
    
]