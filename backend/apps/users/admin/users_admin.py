from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from apps.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
