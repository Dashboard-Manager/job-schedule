from config.env import env
from config.settings.base import *  # noqa
import socket

DEBUG = True

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = [env("ALLOWED_HOSTS")]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "NAME": env("POSTGRES_DB"),
#         "USER": env("POSTGRES_USER"),
#         "PASSWORD": env("POSTGRES_PASSWORD"),
#         "HOST": env("POSTGRES_HOST"),
#         "PORT": env("POSTGRES_PORT"),
#     }
# }


INSTALLED_APPS += [  # noqa F405
    "debug_toolbar",
]
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa F405
DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
}

INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]

hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS += [".".join(ip.split(".")[:-1] + ["1"]) for ip in ips]
