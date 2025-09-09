from django.apps import AppConfig


class BarbershopsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.v1.barbershops'
    label = 'barbershops'

    def ready(self):
        import apps.v1.shared.patches  # noqa