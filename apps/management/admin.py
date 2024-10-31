from django.contrib import admin

from apps.management.models import Device


# Register your models here.
@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('ae_id', 'ae_rn', 'hardware_id', 'asset_number', 'name', 'date', 'owner', 'user', 'version', 'status', 'location', 'type')