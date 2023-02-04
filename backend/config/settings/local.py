from config.env import env
from config.settings.base import *  # noqa

# General
DEBUG = True

SECRET_KEY = env(
    "SECRET_KEY",
    default="FRONTENDOWIEC-ZAPRASZAMY",
)

# Databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "db_local.sqlite3",
    }
}

# Cache
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}

# Django-debug-toolbar

INSTALLED_APPS += [  # noqa
    "debug_toolbar",
]

MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa

DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    "SHOW_TEMPLATE_CONTEXT": True,
}


# Runserver-plus conf
RUNSERVERPLUS_SERVER_ADDRESS_PORT = "0.0.0.0:8000"

SHELL_PLUS = "ipython"

SHELL_PLUS_PRINT_SQL = True

NOTEBOOK_ARGUMENTS = [
    "--ip",
    "0.0.0.0",
    "--port",
    "8000",
    "--allow-root",
    "--no-browser",
]

IPYTHON_ARGUMENTS = [
    "--ext",
    "django_extensions.management.notebook_extension",
    "--debug",
]

IPYTHON_KERNEL_DISPLAY_NAME = "Django Shell-Plus"

INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]
