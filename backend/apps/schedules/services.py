def get_hours(end_job, start_job):
    return divmod((end_job - start_job).total_seconds(), 3600)[0]
