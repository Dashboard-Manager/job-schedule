# TODO: Create function to return quantity of hours from current/last month, year and week from job model for specific user
from apps.schedules.models import Job
from apps.users.models import Profile
from django.db import models


def get_working_hours(
    user: Profile, start_date: models.DateField, end_date: models.DateField
) -> int:
    working_days = Job.objects.filter(
        date__range=(start_date, end_date),
        user=user,
    )
    total_hours = sum([job.job_hours for job in working_days])
    return int(total_hours)
