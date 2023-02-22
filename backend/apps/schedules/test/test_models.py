import datetime

import pytest
from apps.schedules.services import get_hours
from apps.schedules.test.factory import JobFactory


@pytest.mark.django_db
class TestJob:
    @pytest.fixture
    def job(self, *args, **kwargs):
        return JobFactory.create(*args, **kwargs)

    def test_str_job(self, job):
        assert (
            str(job) == f"{job.user} worked by {job.hours} and {job.extra_hours} hours"
        )

    def test_hours(self, job):
        assert job.hours == min(
            divmod((job.start_job - job.end_job).total_seconds(), 3600)[0], 8
        )

    def test_extra_hours(self, job):
        assert job.extra_hours == max(
            0, divmod((job.start_job - job.end_job).total_seconds(), 3600)[0] - 8
        )

    def test_get_hours(self):
        start_job_str = "2022-02-22T10:00:00"
        end_job_str = "2022-02-22T12:30:00"
        expected_hours = 2
        # start_job = datetime.datetime.strptime(start_job_str, "%Y-%m-%dT%H:%M:%S")
        # end_job = datetime.datetime.strptime(end_job_str, "%Y-%m-%dT%H:%M:%S")

        start_job = datetime.datetime.fromisoformat(start_job_str)
        end_job = datetime.datetime.fromisoformat(end_job_str)

        assert get_hours(start_job=start_job_str, end_job=end_job_str) == expected_hours
        assert get_hours(start_job, end_job) == expected_hours
