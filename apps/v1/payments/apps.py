from django.apps import AppConfig


class PaymentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.v1.payments'
    label = 'payments'

    def ready(self):
        import apps.v1.shared.patches  # noqa