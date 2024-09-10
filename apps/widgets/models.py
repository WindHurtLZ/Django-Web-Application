from django.db import models

from apps.home.models import Device


# Create your models here.
class Map(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='paths')
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.device.name} at {self.latitude}, {self.longitude}"