from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Device(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('updating', 'Updating'),
    ]

    name = models.CharField(max_length=100)
    date = models.DateField(autonow_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    version = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    battery = models.IntegerField(default=0)
    location = models.CharField(max_length=100)
    type = models.CharField(max_length=50)

    def __str__(self):
        return "%s: %s" % (self.owner, self.name)

