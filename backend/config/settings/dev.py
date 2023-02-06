import os
import socket  # noqa

import environ
from config.env import ENV_DIR, env
from config.settings.base import *  # noqa

environ.Env.read_env(os.path.join(ENV_DIR, "postgres.env"))
environ.Env.read_env(os.path.join(ENV_DIR, "docker.env"))

DEBUG = env.bool("DEBUG")
# Generals
SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

# Databases

DATABASES = {"default": env.db("DATABASE_URL")}
DATABASES["default"]["ATOMIC_REQUESTS"] = True


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
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS += [".".join(ip.split(".")[:-1] + ["1"]) for ip in ips]  # noqa

# Email

# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
# EMAIL_BACKEND = env(
#     "DJANGO_EMAIL_BACKEND",
#     default="django.core.mail.backends.smtp.EmailBackend",
# )
# # https://docs.djangoproject.com/en/dev/ref/settings/#email-timeout
# EMAIL_TIMEOUT = 5
