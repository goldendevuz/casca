from django.apps import AppConfig


class SettingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.v1.settings'
    label = 'settings'

    def ready(self):
        import apps.v1.shared.patches  # noqa