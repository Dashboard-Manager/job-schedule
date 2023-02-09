from apps.earnings.models import (  # JobHours,
    Calculations,
    Constants,
    Salaries,
    Settlements,
)
from apps.users.models import Profile
from django.contrib import admin

admin.site.register([Settlements, Calculations, Constants])
admin.site.register([Settlements, Calculations, Constants])


# @admin.register(Constants, Calculations, Salaries, Settlements)
# class EarningsAdmin(admin.ModelAdmin):  # type: ignore
#     list_display = [
#         "Settlements.user",
#         "Salaries.brutto_salary",
#         "Salaries.netto_salary",
#     ]
#     readonly_fields = [
#         "brutto_salary",
#         "netto_salary",
#         "pension_contribution",
#         "disability_contribution",
#         "sickness_contribution",
#         "ZUS_contributions",
#         "health_care_contribution",
#         "income",
#         "income_tax",
#     ]
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
        "user",
        "ZUS_contributions",
    ]
    readonly_fields = [
        "ZUS_contributions",
    ]


class ProfileInLine(admin.TabularInline):  # type: ignore
    model = Profile


admin.site.register([Constants, Calculations, Salaries, Settlements])

# @admin.register(Constants, Calculations, Salaries, Settlements)
# class EarningsAdmin(admin.ModelAdmin):  # type: ignore
#     list_display = [
#         "Settlements.user",
#         "Salaries.brutto_salary",
#         "Salaries.netto_salary",
#     ]
#     readonly_fields = [
#         "brutto_salary",
#         "netto_salary",
#         "pension_contribution",
#         "disability_contribution",
#         "sickness_contribution",
#         "ZUS_contributions",
#         "health_care_contribution",
#         "income",
#         "income_tax",
#     ]

#     fieldsets = (
#         (
#             "Profile informations",
#             {
#                 "fields": (
#                     "user",
#                     "age",
#                 )
#             },
#         ),
#         (
#             "Salary informations",
#             {
#                 "classes": (
#                     "wide",
#                     "extrapretty",
#                 ),
#                 "fields": (
#                     (
#                         "brutto_salary",
#                         "netto_salary",
#                     ),
#                 ),
#             },
#         ),
#         (
#             "Constants for calculations",
#             {
#                 "classes": ("wide",),
#                 "fields": (
#                     "constant_pension_contribution",
#                     "constant_disability_contribution",
#                     "constant_sickness_contribution",
#                     "constant_health_care_contribution",
#                     "constant_PIT",
#                 ),
#             },
#         ),
#         (
#             "Earnings informations",
#             {
#                 "classes": (
#                     "wide",
#                     "extrapretty",
#                 ),
#                 "fields": (
#                     (
#                         "pension_contribution",
#                         "disability_contribution",
#                         "sickness_contribution",
#                     ),
#                     ("ZUS_contributions",),
#                     "health_care_contribution",
#                     (
#                         "income",
#                         "income_tax",
#                     ),
#                 ),
#             },
#         ),
#     )
#     add_fieldsets = ()

# @admin.register(JobHours)
# class JobAdmin(admin.ModelAdmin):  # type: ignore
#     list_display = [
#         "user",
#         "start_date",
#         "end_date",
#         "hours",
#         "extra_hours",
#     ]

# @admin.register(JobHours)
# class JobAdmin(admin.ModelAdmin):  # type: ignore
#     list_display = [
#         "user",
#         "start_date",
#         "end_date",
#         "hours",
#         "extra_hours",
#     ]

#     readonly_fields = [
#         "hours",
#         "extra_hours",
#     ]
#     fieldsets = (
#         (
#             "Profile informations",
#             {
#                 "fields": (
#                     "user",
#                     "hours",
#                     "extra_hours",
#                 )
#             },
#         ),
#         (
#             "Find hours between dates..",
#             {
#                 "classes": (
#                     "wide",
#                     "extrapretty",
#                 ),
#                 "fields": (
#                     (
#                         "start_date",
#                         "end_date",
#                     ),
#                 ),
#             },
#         ),
#     )
