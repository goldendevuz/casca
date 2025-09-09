from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.v1.accounts'
    label = 'accounts'

    def ready(self):
        import apps.v1.shared.patches  # noqa
        import apps.v1.accounts.signals # noqa
