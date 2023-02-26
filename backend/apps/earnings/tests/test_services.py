from datetime import date

import pytest
from apps.earnings.services.calculations import (
    calc_disability_contr,
    calc_health_care_contr,
    calc_income,
    calc_income_tax,
    calc_pension_contr,
    calc_sickness_contr,
)
from apps.earnings.services.working_hours import get_working_hours
from apps.schedules.tests.factory import JobFactory
from apps.users.tests.factory import UserFactory


class TestCalculations:
    def test_calc_pension_contr(self):
        assert calc_pension_contr(10000, 19.5) == 1950.00
        assert calc_pension_contr(0, 19.5) == 0.00
        assert calc_pension_contr(10000, 0) == 0.00
        assert calc_pension_contr(10000, 100) == 10000.00
        assert calc_pension_contr(10000, 12.3456) == 1234.56

    def test_calc_disability_contr(self):
        assert calc_disability_contr(10000, 8) == 800.00
        assert calc_disability_contr(0, 8) == 0.00
        assert calc_disability_contr(10000, 0) == 0.00
        assert calc_disability_contr(10000, 100) == 10000.00
        assert calc_disability_contr(10000, 2.3456) == 234.56

    def test_calc_sickness_contr(self):
        assert calc_sickness_contr(10000, 2.45) == 245.00
        assert calc_sickness_contr(0, 2.45) == 0.00
        assert calc_sickness_contr(10000, 0) == 0.00
        assert calc_sickness_contr(10000, 100) == 10000.00
        assert calc_sickness_contr(10000, 0.3456) == 34.56

    def test_calc_health_care_contr(self):
        assert calc_health_care_contr(10000, 1100, 9) == 801.00
        assert calc_health_care_contr(0, 0, 9) == 0.00
        assert calc_health_care_contr(10000, 0, 9) == 900.00
        assert calc_health_care_contr(10000, 10000, 9) == 0.00
        assert calc_health_care_contr(10000, 1000, 3.45) == 310.5

    def test_calc_income(self):
        assert calc_income(10000, 1100) == 8650.00
        assert calc_income(0, 0) == 0.00
        assert calc_income(10000, 0) == 9750.00
        assert calc_income(10000, 10000) == 0.00
        assert calc_income(10000, 2500) == 7250.00

    def test_calc_income_tax(self):
        assert calc_income_tax(10000, 18) == 1500
        assert calc_income_tax(0, 18) == 0
        assert calc_income_tax(10000, 0) == 0
        assert calc_income_tax(10000, 100) == 9700
        assert calc_income_tax(10000, 12) == 900


@pytest.mark.django_db
class TestWorkingHours:
    @pytest.fixture
    def user(self):
        user = UserFactory.create()

        return user

    @pytest.fixture
    def job(self, user):
        return JobFactory.create(user=user)

    def test_get_working_hours(self, user, job):
        result = get_working_hours(user, job.date, job.date, extra_hours=False)
        assert result == 0  # TODO: Create JobFactory

        result = get_working_hours(
            user, date(2022, 1, 1), date(2022, 1, 2), extra_hours=True
        )
        assert result == 0  # TODO: Create JobFactory

        result = get_working_hours(
            user, date(2022, 1, 4), date(2022, 1, 5), extra_hours=False
        )
        assert result == 0  # TODO: Create JobFactory

        result = get_working_hours(
            None, date(2022, 1, 1), date(2022, 1, 2), extra_hours=False
        )
        assert result == 0  # TODO: Create JobFactory
