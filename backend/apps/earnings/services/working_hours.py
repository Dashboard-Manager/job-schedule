from datetime import date

from apps.schedules.models import Job
from django.contrib.auth.models import User


def get_working_hours(
    user: User, start_date: date, end_date: date, extra_hours: bool = False
) -> int:
    try:
        working_days = Job.objects.filter(
            date__range=(start_date, end_date),
            user=user,
        )
        total_hours = sum(
            [job.extra_hours if extra_hours else job.hours for job in working_days]
        )
    except Job.DoesNotExist:
        return 0
    return int(total_hours)
