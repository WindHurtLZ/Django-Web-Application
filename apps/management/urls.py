from django.urls import include, path

from apps.management import views
from apps.management.views import receive_notification

urlpatterns = [

    path('', views.root_view, name='root'),
    path('index/', views.index, name='management'),
    path('device/', views.device, name='device'),
    path('add_device/', views.add_device, name='add_device'),
    path('delete_device/', views.delete_device, name='delete_device'),

    # Important Note, do not add / behind the notifications, OneM2M will ignore the last / when it sends any info
    path('notifications', views.receive_notification, name='receive_notification'),
    path('firmware_list/', views.firmware_list, name='firmware_list'),
    path('upload_firmware/', views.upload_firmware, name='upload_firmware'),
    path('delete_firmware/', views.delete_firmware, name='delete_firmware'),
    path('update_device_firmware/', views.update_device_firmware, name='update_device_firmware'),
]