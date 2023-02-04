from config.env import env
from config.settings.base import *  # noqa

DEBUG = True

SECRET_KEY = env(
    "SECRET_KEY",
    default="FRONTENDOWIEC-ZAPRASZAMY",
)

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


INSTALLED_APPS += [  # noqa
    "debug_toolbar",
]
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa

DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
}
