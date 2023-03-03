import os
import socket
import sys

import environ

from config.env import BACKEND_DIR, ENV_DIR, env
from config.settings.base import *  # noqa

environ.Env.read_env(os.path.join(ENV_DIR, "postgres.env"))
environ.Env.read_env(os.path.join(ENV_DIR, "docker.env"))

# PATHS
path_list = [
    BACKEND_DIR / "apps",
    BACKEND_DIR / "config",
    ENV_DIR,
]
sys.path.extend([str(path_dir) for path_dir in path_list])

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env("SECRET_KEY")
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool("DEBUG")
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

# django-debug-toolbar
# ------------------------------------------------------------------------------
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#prerequisites
INSTALLED_APPS += [  # noqa F405
    "debug_toolbar",
]
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#middleware
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa F405
# https://django-debug-toolbar.readthedocs.io/en/latest/configuration.html#debug-toolbar-config
DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
}
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#internal-ips
INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]

# Docker support
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#configure-internal-ips
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS += [".".join(ip.split(".")[:-1] + ["1"]) for ip in ips]

if os.environ.get("RUN_MAIN") or os.environ.get("WERKZEUG_RUN_MAIN"):
    import debugpy  # noqa: E402

    debugpy.listen(("0.0.0.0", 7777))
    print("========== DJANGO DEBUGPY ==========")  # noqa: T201
