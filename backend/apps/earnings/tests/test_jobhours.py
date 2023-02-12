import datetime

import pytest
from apps.earnings.models import JobHours
from apps.earnings.tests.factory import JobHoursFactory
from apps.users.models import Profile
from django.core.exceptions import ValidationError


class JobHoursTest:
    @pytest.fixture
    def jobhours(self):
        return JobHoursFactory.create()

    def test_instance_jobhours(self, jobhours):
        assert isinstance(jobhours, JobHours)
        assert isinstance(jobhours.date, datetime.date)
        assert isinstance(jobhours.user, Profile)
        assert isinstance(jobhours.start_date, datetime.date)
        assert isinstance(jobhours.end_date, datetime.date)
        assert isinstance(jobhours.hours, int)
        assert isinstance(jobhours.extra_hours, int)

    def test_time_job_validation(self, jobhours):
        with pytest.raises(ValidationError) as e:
            jobhours.full_clean()
        assert "End date must be after start date" in str(e.value)
