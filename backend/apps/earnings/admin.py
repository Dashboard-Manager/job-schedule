from apps.earnings.models import Calculations, Constants, JobHours, Settlements
from django.contrib import admin


@admin.register(Settlements)
class SettlementsAdmin(admin.ModelAdmin):
    list_display = [
        "date",
        "user",
        "calculations",
    ]


@admin.register(Constants)
class ConstantsAdmin(admin.ModelAdmin):
    list_display = [
        "date",
        "PIT",
        "pension_contribution",
        "disability_contribution",
        "sickness_contribution",
        "health_care_contribution",
    ]


@admin.register(Calculations)
class CalculationsAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "brutto_salary",
        "netto_salary",
    ]
    readonly_fields = [
        "pension_contribution",
        "disability_contribution",
        "sickness_contribution",
        "health_care_contribution",
        "income",
        "income_tax",
        "netto_salary",
    ]


@admin.register(JobHours)
class JobAdmin(admin.ModelAdmin):  # type: ignore
    list_display = [
        "user",
        "start_date",
        "end_date",
        "hours",
        "extra_hours",
    ]

    readonly_fields = [
        "hours",
        "extra_hours",
    ]
    fieldsets = (
        (
            "Profile informations",
            {
                "fields": (
                    "user",
                    "hours",
                    "extra_hours",
                )
            },
        ),
        (
            "Find hours between dates..",
            {
                "classes": (
                    "wide",
                    "extrapretty",
                ),
                "fields": (
                    (
                        "start_date",
                        "end_date",
                    ),
                ),
            },
        ),
    )
