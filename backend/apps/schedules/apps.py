from django.apps import AppConfig


class SchedulesConfig(AppConfig):
    name = "apps.schedules"
    verbose_name = "Schedules"

    def ready(self):
        import apps.schedules.signals  # noqa
