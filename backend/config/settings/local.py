import os

import environ
from config.env import ENV_DIR, env
from config.settings.base import *  # noqa

environ.Env.read_env(os.path.join(ENV_DIR, "postgres.env"))
environ.Env.read_env(os.path.join(ENV_DIR, "local.env"))

DEBUG = env.bool("DEBUG")
# Generals
SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": "",
        "PORT": 5433,
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
