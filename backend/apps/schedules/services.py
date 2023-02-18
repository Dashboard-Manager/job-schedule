from datetime import datetime


def get_hours(start_job: datetime, end_job: datetime):
    return int(divmod((start_job - end_job).total_seconds(), 3600)[0])


def get_job_hours(start_job: datetime, end_job: datetime):
    hours = get_hours(end_job, start_job)  # noqa
    return min(hours, 8.0)


def get_extra_job_hours(start_job: datetime, end_job: datetime):
    hours = get_hours(end_job, start_job)  # noqa
    return max(0, hours - 8)
