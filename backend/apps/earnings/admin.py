from apps.earnings.models import Earnings
from django.contrib import admin


@admin.register(Earnings)
class EarningsAdmin(admin.ModelAdmin):  # type: ignore
    list_display = [
        "user",
        "brutto_salary",
        "netto_salary",
        "pension_contribution",
        "disability_contribution",
        "sickness_contribution",
        "ZUS_contributions",
        "health_care_contribution",
        "income",
        "income_tax",
    ]
    readonly_fields = [
        "brutto_salary",
        "netto_salary",
        "pension_contribution",
        "disability_contribution",
        "sickness_contribution",
        "ZUS_contributions",
        "health_care_contribution",
        "income",
        "income_tax",
    ]
