import pytest
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
