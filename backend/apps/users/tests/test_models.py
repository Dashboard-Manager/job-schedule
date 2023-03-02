from datetime import date, timedelta

import pytest
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from apps.users.tests.factory import ProfileFactory


@pytest.mark.django_db
class TestProfileModel:
    @pytest.fixture
    def profile(self):
        return ProfileFactory.create()

    def custom_profile(self, *args, **kwargs):
        return ProfileFactory.build(*args, **kwargs)

    def test_str(self, profile):
        assert str(profile) == profile.username

    def test_instance_salary(self, profile):
        assert isinstance(profile.salary, float)

    def test_salary_validation(self):
        instance = self.custom_profile(salary=-1)  # noqa
        with pytest.raises(ValidationError) as exception:
            instance.full_clean()
        assert "Salary cannot be less than 0" in str(exception.value)

        instance = self.custom_profile(salary=0)  # noqa
        instance.full_clean()

        instance = self.custom_profile(salary=10_000_000_000)  # noqa
        with pytest.raises(ValidationError) as exception:
            instance.full_clean()
        assert "Sorry, but we need to have some limits" in str(exception.value)

        instance = self.custom_profile(salary=3700)  # noqa
        instance.full_clean()

    def test_birth_date_instance(self, profile):
        assert isinstance(profile.birth_date, date)

    def test_birth_validations(self):
        instance = self.custom_profile(birth_date=date.today())  # noqa
        with pytest.raises(ValidationError) as exception:
            instance.full_clean()
        assert "You are too young to use this application." in str(exception.value)

        instance = self.custom_profile(  # noqa
            birth_date=(date.today() + timedelta(days=1)),
        )
        with pytest.raises(ValidationError) as exception:
            instance.full_clean()
        assert "The birth date cannot be in the past.." in str(exception.value)

        instance = self.custom_profile(  # noqa
            birth_date=(date.today() - timedelta(days=16 * 366))
        )
        instance.full_clean()

    def test_age_instance(self, profile):
        assert isinstance(profile.age, int)

    def test_age_validations(self):
        instance = self.custom_profile(birth_date=date(1999, 6, 9))  # noqa
        assert instance.age == 24

        instance = self.custom_profile(birth_date=None)  # noqa
        assert instance.age == 0

    def test_absolute_url(self, profile):
        assert profile.get_absolute_url() == f"profile/{profile.username}/"


class TestUser:
    @pytest.fixture
    def user_data(
        self,
    ):
        return {
            "username": "Robert",
            "password": "robert123",
        }

    def test_user_data_username(self, user_data):
        User = get_user_model()
        user = User(**user_data)
        assert user.username == "Robert"

    def test_user_data_password(self, user_data):
        User = get_user_model()
        user = User(**user_data)
        assert user.password == "robert123"
