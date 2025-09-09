from django.apps import AppConfig


class MessagingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.v1.messaging'
    label = 'messaging'

    def ready(self):
        import apps.v1.shared.patches  # noqa