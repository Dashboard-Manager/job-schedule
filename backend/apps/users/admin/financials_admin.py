from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from apps.users.models import Financials


@admin.register(Financials)
class FinancialsAdmin(admin.ModelAdmin):
    list_display = [
        "salary",
        "hourly_pay",
        "extra_hourly_pay",
        "is_student",
    ]
