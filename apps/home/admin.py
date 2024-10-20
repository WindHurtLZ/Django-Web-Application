from django.contrib import admin

from apps.home.models import Ride


# Register your models here.
@admin.register(Ride)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('user', 'device', 'start_time', 'end_time')