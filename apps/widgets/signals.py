# signals.py

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils import timezone
from .models import MeshConnectivity
from . import views

@receiver([post_save, post_delete], sender=MeshConnectivity)
def update_last_modified(sender, instance, **kwargs):
    views.last_update_time = timezone.now()
