from django.db import models

from apps.management.models import Device


# Create your models here.
class DeviceData(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='data')
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    temperature = models.FloatField(null=True, blank=True)
    speed = models.FloatField(null=True, blank=True)
    acceleration = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.device.name} at {self.latitude}, {self.longitude}"

class MeshConnectivity(models.Model):
    device = models.OneToOneField(Device, on_delete=models.CASCADE, related_name='mesh_connectivity')
    parent_id = models.CharField(max_length=100, null=True, blank=True)
    stnr = models.IntegerField(null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"MeshConnectivity for {self.device.name}"

class Battery(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='battery')
    battery_percentage = models.IntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Battery for {self.device.name} at {self.timestamp}"
