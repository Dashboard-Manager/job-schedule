from datetime import date

from apps.schedules.models import Job
from apps.users.models import Profile


def get_working_hours(
    user: Profile, start_date: date, end_date: date, extra_hours: bool = False
) -> int:
    working_days = Job.objects.filter(
        date__range=(start_date, end_date),
        user=user,
    )
    total_hours = sum(
        [job.extra_job_hours if extra_hours else job.job_hours for job in working_days]
    )
    return int(total_hours)
