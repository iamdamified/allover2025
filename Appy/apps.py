from django.apps import AppConfig


class AppyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Appy'

    def ready(self):
        import Appy.signals #used to import signals.py
