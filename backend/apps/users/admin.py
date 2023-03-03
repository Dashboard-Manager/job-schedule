from django.contrib import admin

from apps.users.models import Financials, Profile, User
from apps.users.forms import UserAdminChangeForm, UserAdminCreationForm
from django.contrib.auth import admin as auth_admin
from django.utils.translation import gettext_lazy as _


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["email", "first_name", "last_name", "is_superuser"]
    search_fields = ["first_name", "last_name"]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "identificator",
        "birth_date",
        "age",
    ]
    readonly_fields = [
        "identificator",
        "age",
    ]


@admin.register(Financials)
class FinancialsAdmin(admin.ModelAdmin):
    list_display = [
        "profile",
        "salary",
        "hourly_pay",
        "extra_hourly_pay",
        "is_student",
    ]
