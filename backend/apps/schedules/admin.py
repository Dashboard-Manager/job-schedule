from apps.schedules.models import Event, Job
from django.contrib import admin

admin.site.register(Event)


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):  # type: ignore
    list_display = [
        "user",
        "date",
        "hours",
        "extra_hours",
    ]
    readonly_fields = [
        "hours",
        "extra_hours",
    ]

    fieldsets = (
        (
            "Employer informations",
            {
                "fields": (
                    "user",
                    "hours",
                    "extra_hours",
                    "date",
                )
            },
        ),
        (
            "Working hours",
            {
                "fields": (
                    (
                        "start_job",
                        "end_job",
                    ),
                )
            },
        ),
    )
