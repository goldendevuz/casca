from django.apps import AppConfig


class AppointmentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.v1.appointments'
    label = 'appointments'

    def ready(self):
        import apps.v1.shared.patches  # noqa