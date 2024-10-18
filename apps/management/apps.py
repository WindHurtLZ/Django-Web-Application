from django.apps import AppConfig

from apps.management.onem2m_scheduler import start_scheduler


class ManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.management'

    def ready(self):
        start_scheduler()
        import apps.management.signals