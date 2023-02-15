from apps.users.models import Financials, Profile
from django.contrib import admin

# from django.utils.translation import gettext_lazy as _

admin.site.register(Profile)
admin.site.register(Financials)
