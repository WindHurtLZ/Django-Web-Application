from django.contrib import admin

from apps.widgets.models import DeviceData, MeshConnectivity, Battery


# Register your models here.
@admin.register(DeviceData)
class DeviceDataAdmin(admin.ModelAdmin):
    list_display = ('device', 'latitude', 'longitude', 'temperature', 'speed', 'timestamp')

@admin.register(MeshConnectivity)
class MeshConnectivityAdmin(admin.ModelAdmin):
    list_display = ('device', 'parent_id', 'rssi', 'last_updated')

@admin.register(Battery)
class BatteryAdmin(admin.ModelAdmin):
    list_display = ('device', 'battery_percentage', 'timestamp')