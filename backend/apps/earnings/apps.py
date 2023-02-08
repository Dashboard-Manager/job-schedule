from django.apps import AppConfig


class EarningsConfig(AppConfig):
    name = "apps.earnings"
    verbose_name = "Reckoning panel"

    def ready(self):
        import apps.earnings.signals  # noqa
