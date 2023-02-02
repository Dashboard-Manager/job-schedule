from datetime import datetime


def get_hours(
    end_job: datetime,
    start_job: datetime,
):
    return int(divmod((end_job - start_job).total_seconds(), 3600)[0])
