from django.contrib import admin

from apps.widgets.models import Map


# Register your models here.
@admin.register(Map)
class MapAdmin(admin.ModelAdmin):
    list_display = ('device', 'latitude', 'longitude', 'timestamp')