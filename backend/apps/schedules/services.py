from datetime import datetime
from typing import Union


def get_hours(start_job: Union[datetime, str], end_job: Union[datetime, str]):
    if isinstance(start_job, str):
        start_job = datetime.isoformat(start_job)  # type: ignore

    if isinstance(end_job, str):
        end_job = datetime.isoformat(end_job)  # type: ignore

    return int(divmod((start_job - end_job).total_seconds(), 3600)[0])  # type: ignore


def get_job_hours(start_job: datetime, end_job: datetime):
    hours = get_hours(end_job, start_job)  # noqa
    return min(hours, 8.0)


def get_extra_job_hours(start_job: datetime, end_job: datetime):
    hours = get_hours(end_job, start_job)  # noqa
    return max(0, hours - 8)
