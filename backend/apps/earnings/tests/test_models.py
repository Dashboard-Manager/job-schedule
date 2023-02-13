import datetime

import pytest
from apps.earnings.tests.factory import JobHoursFactory
from apps.users.models import Profile
from django.core.exceptions import ValidationError
from django.utils import timezone


@pytest.mark.django_db
class TestJobHours:
    @pytest.fixture
    def jobhours(self):
        return JobHoursFactory.create()

    def test_str_jobhours(self, jobhours):
        assert str(jobhours) == f"{jobhours.user} has {jobhours.hours} hours in date"

    def test_instance_jobhours(self, jobhours):
        assert isinstance(jobhours.date, timezone.datetime)
        assert isinstance(jobhours.user, Profile)
        assert isinstance(jobhours.start_date, datetime.date)
        assert isinstance(jobhours.end_date, datetime.date)
        assert isinstance(jobhours.hours, int)
        assert isinstance(jobhours.extra_hours, int)

    def test_limits_for_hours(self, jobhours):
        instance = JobHoursFactory(hours=0)
        instance.full_clean()

        instance = JobHoursFactory(hours=-1)
        with pytest.raises(ValidationError) as exception:
            instance.full_clean()
        assert "Working hours cannot be less than 0" in str(exception.value)

        instance = JobHoursFactory(extra_hours=0)
        instance.full_clean()

        instance = JobHoursFactory(extra_hours=-1)
        with pytest.raises(ValidationError) as exception:
            instance.full_clean()
        assert "Working hours cannot be less than 0" in str(exception.value)

    def test_time_job_validation(self):
        instance = JobHoursFactory(start_date="1999-06-09", end_date="2022-06-09")
        instance.full_clean()

        instance = JobHoursFactory(end_date="1999-06-09", start_date="2022-06-09")
        with pytest.raises(ValidationError) as e:
            instance.full_clean()
        assert "End date must be after start date" in str(e.value)
