from django.apps import AppConfig


class WidgetsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.widgets'

    def ready(self):
        import apps.widgets.signals