from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

from apps.management.models import Device


class Ride(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rides')
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='rides')
    start_time = models.DateTimeField(auto_now_add=True)  # Ride Start Time
    end_time = models.DateTimeField(null=True, blank=True)  # End Time

    def get_duration(self):
        if self.end_time:
            return (self.end_time - self.start_time).total_seconds()
        else:
            from django.utils import timezone
            return (timezone.now() - self.start_time).total_seconds()

    def __str__(self):
        return f"Ride by {self.user} on {self.device.name}"
