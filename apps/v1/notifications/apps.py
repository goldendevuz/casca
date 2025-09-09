from django.apps import AppConfig


class NotificationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.v1.notifications'
    label = 'notifications'

    def ready(self):
        import apps.v1.shared.patches  # noqa