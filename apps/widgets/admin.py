from django.contrib import admin

from apps.widgets.models import DeviceData


# Register your models here.
@admin.register(DeviceData)
class DeviceDataAdmin(admin.ModelAdmin):
    list_display = ('device', 'latitude', 'longitude', 'temperature', 'speed', 'timestamp')