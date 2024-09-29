from django.apps import AppConfig

from apps.home.onem2m_scheduler import start_scheduler


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.home'

    def ready(self):
        start_scheduler()
        import apps.home.signals