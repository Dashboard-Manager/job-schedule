from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = "apps.users"
    verbose_name = "Employer Profile"

    def ready(self):
        import apps.users.signals  # noqa
