from config.env import env
from config.settings.base import *  # noqa

DEBUG = True

SECRET_KEY = env(
    "SECRET_KEY",
    default="FRONTENDOWIEC-ZAPRASZAMY",
)

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env("POSTGRES_DB", default="postgres_db"),
        "USER": env("POSTGRES_USER", default="postgres_user"),
        "PASSWORD": env("POSTGRES_PASSWORD", default="postgres_pass"),
        "HOST": env("POSTGRES_HOST", default="postgres"),
        "PORT": env("POSTGRES_PORT", default="5432"),
    }
}


INSTALLED_APPS += [  # noqa
    "debug_toolbar",
]
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa

DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
}
