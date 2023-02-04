import socket  # noqa

from config.env import env

try:  # noqa
    from config.settings.local import *  # noqa
except ImportError:
    pass

# Generals
SECRET_KEY = env("SECRET_KEY", default="random_few_signs")

ALLOWED_HOSTS = env("ALLOWED_HOSTS", default=["localhost", "0.0.0.0", "127.0.0.1"])

# Databases

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

hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS += [".".join(ip.split(".")[:-1] + ["1"]) for ip in ips]  # noqa
