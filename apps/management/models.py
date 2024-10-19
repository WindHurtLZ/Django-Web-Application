import uuid

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Device(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('updating', 'Updating'),
    ]

    ae_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    ae_rn = models.CharField(max_length=100)
    hardware_id = models.CharField(max_length=5, unique=True)
    asset_number = models.CharField(max_length=4, unique=True)
    name = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_devices')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='used_devices')
    version = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    battery = models.IntegerField(default=0)
    location = models.CharField(max_length=100)
    type = models.CharField(max_length=50)

    def __str__(self):
        return "%s: %s" % (self.owner, self.name)

    def save(self, *args, **kwargs):
        if not self.asset_number:
            self.asset_number = self.generate_asset_number()
        super(Device, self).save(*args, **kwargs)

    @staticmethod
    def generate_asset_number():
        # Search last asset number
        last_device = Device.objects.filter(asset_number__isnull=False).order_by('-asset_number').first()
        if last_device:
            last_number = int(last_device.asset_number)
            new_number = last_number + 1
        else:
            new_number = 0

        # formate to 4 digit
        return f"{new_number:04d}"

    def __str__(self):
        return "%s: %s" % (self.owner, self.name)

