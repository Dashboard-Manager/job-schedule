from apps.schedules.models import Event, Job
from django.contrib import admin

admin.site.register(Event)


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):  # type: ignore
    list_display = [
        "user",
        "date",
        "job_hours",
        "extra_job_hours",
    ]
    readonly_fields = [
        "job_hours",
        "extra_job_hours",
    ]

    fieldsets = (
        (
            "Employer informations",
            {
                "fields": (
                    "user",
                    "job_hours",
                    "extra_job_hours",
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
