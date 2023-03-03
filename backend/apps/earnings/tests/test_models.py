import datetime

import pytest
from apps.earnings import signals
from apps.earnings.models import Constants
from apps.earnings.tests.factory import (
    CalculationsFactory,
    ConstantsFactory,
    JobHoursFactory,
)
from apps.users.tests.factory import UserFactory
from apps.users.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone
from factory.django import mute_signals


@pytest.mark.django_db
class TestConstants:
    @pytest.fixture
    def constants(self):
        return ConstantsFactory.create()

    def test_str_constant(self, constants):
        assert str(constants) == f"Constants at {constants.date}"


@pytest.mark.django_db
class TestJobHours:
    @pytest.fixture
    def jobhours(self):
        return JobHoursFactory.create()

    def test_str_jobhours(self, jobhours):
        assert (
            str(jobhours)
            == f"{jobhours.user} has {jobhours.hours} hours and {jobhours.extra_hours} extra hours"
        )

    def test_instance_jobhours(self, jobhours):
        assert isinstance(jobhours.date, timezone.datetime)
        assert isinstance(jobhours.user, User)
        assert isinstance(jobhours.start_date, datetime.date)
        assert isinstance(jobhours.end_date, datetime.date)
        assert isinstance(jobhours.hours, int)
        assert isinstance(jobhours.extra_hours, int)

    @mute_signals(signals.pre_save)
    def test_limits_for_hours(self, jobhours):
        instance = JobHoursFactory(hours=0)
        instance.full_clean()

        instance = JobHoursFactory.create(hours=-1)
        # pdb.set_trace()
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


@pytest.mark.django_db
class TestCalculations:
    @pytest.fixture
    def calculations(self):
        constants = ConstantsFactory.create()

        user = UserFactory.create()
        return CalculationsFactory(constants=constants, user=user)

    def custom_calculations(self, *args, **kwargs):
        return CalculationsFactory.create(*args, **kwargs)

    def test_str_calculations(self, calculations):
        assert (
            str(calculations)
            == f"{calculations.user} earned {calculations.netto_salary} PLN"
        )

    def test_netto_salary(self):  # noqa
        calculated_netto_for_less_than_26 = 2784.21
        user = UserFactory.create()
        user.profile.financials.salary = 3600
        user.profile.birth_date = self.get_age(26)  # noqa
        constants = Constants.objects.create()
        instance = self.custom_calculations(constants=constants, user=user)  # noqa
        assert instance.netto_salary == calculated_netto_for_less_than_26

        calculated_netto_for_more_than_26 = 2784.21
        user = UserFactory.create()
        user.profile.financials.salary = 3600
        user.profile.birth_date = self.get_age(27)
        constants = Constants.objects.create()
        instance = self.custom_calculations(constants=constants, user=user)  # noqa
        assert instance.netto_salary == calculated_netto_for_more_than_26

        user = UserFactory.create()
        user.profile.financials.salary = 3600
        user.profile.birth_date = self.get_age(26)
        user.profile.financials.is_student = True
        constants = Constants.objects.create()
        instance = self.custom_calculations(constants=constants, user=user)  # noqa
        assert instance.netto_salary == 3600

        calculated_netto_for_more_than_26 = 2853.47
        user = UserFactory.create()
        user.profile.financials.salary = 3600
        user.profile.financials.voluntary_health_insurance = False
        user.profile.birth_date = self.get_age(27)
        constants = Constants.objects.create()
        instance = self.custom_calculations(constants=constants, user=user)  # noqa
        assert instance.netto_salary == calculated_netto_for_more_than_26

    @staticmethod
    def get_age(age: int) -> datetime.date:
        today = datetime.date.today()
        return today.replace(year=today.year - age)
