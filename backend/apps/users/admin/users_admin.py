from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from apps.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "name_surname",
        "full_financials",
        "identificator",
        "username_id",
        "email",
        "username",
        "birth_date",
        "last_login",
        "roles",
    )
    list_filter = (
        "birth_date",
        "last_login",
    )
    date_hierarchy = "last_login"
    ordering = ["birth_date", "last_login"]

    def name_surname(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    def full_financials(self, obj):
        text = f""
        text += f"{obj.financial.salary}//"
        text += f"{obj.financial.hourly_pay}//"
        text += f"{obj.financial.extra_hourly_pay}//"
        return text

    def roles(self, obj):
        if obj.is_chief is True:
            return "Chief"
        elif obj.is_team_leader is True:
            return "Team leader"
        elif obj.is_accountant is True:
            return "Accountant"
        else:
            return "Employee"
