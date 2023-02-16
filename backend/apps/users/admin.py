from apps.users.models import Financials, Profile
from django.contrib import admin

# from django.utils.translation import gettext_lazy as _


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
        "user",
        "salary",
        "hourly_pay",
        "extra_hourly_pay",
        "is_student",
    ]
