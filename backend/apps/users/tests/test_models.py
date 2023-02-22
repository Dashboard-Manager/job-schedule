from datetime import date, timedelta

import pytest
from apps.users import signals
from apps.users.tests.factory import FinancialsFactory, ProfileFactory, UserFactory
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import Client
from django.urls import reverse
from factory.django import mute_signals
from pytest_django.asserts import assertQuerysetEqual


@pytest.mark.django_db
class TestUserModel:
    @pytest.fixture
    def user(self):
        return UserFactory.create()

    def test_user_factory(self, user):
        User = get_user_model()
        assert isinstance(user, User)
        assert user.pk is not None
        assert User.objects.filter(pk=user.pk).exists()

    def test_user_factory_with_profile(self, user):
        assert user.profile is not None
        assert user.profile.user == user

    def test_user_factory_batch(self):
        users = UserFactory.create_batch(5)
        User = get_user_model()
        assert len(users) == 5
        assertQuerysetEqual(User.objects.all(), users, ordered=False)


@pytest.mark.django_db
class TestFinancialsMode:
    @pytest.fixture
    @mute_signals(signals.post_save)
    def financials(self):
        user = UserFactory.create()
        profile = ProfileFactory.create(user=user)
        return FinancialsFactory.create(profile=profile)

    @mute_signals(signals.post_save)
    def custom_financials(self, *args, **kwargs):
        user = UserFactory.create()
        profile = ProfileFactory.create(user=user)

        return FinancialsFactory.build(profile=profile, *args, **kwargs)

    def test_str_financials(self, financials):
        assert str(financials) == financials.profile.identificator

    def test_instance_salary(self, financials):
        assert isinstance(financials.salary, (float, int))

    def test_salary_validation(self):
        instance = self.custom_financials(salary=-1)  # noqa
        with pytest.raises(ValidationError) as exception:
            instance.full_clean()
        assert "Salary cannot be less than 0" in str(exception.value)

        instance = self.custom_financials(salary=0)  # noqa
        instance.full_clean()

        instance = self.custom_financials(salary=10_000_000_000)  # noqa
        with pytest.raises(ValidationError) as exception:
            instance.full_clean()
        assert "Sorry, but we need to have some limits" in str(exception.value)

        instance = self.custom_financials(salary=3700)  # noqa
        instance.full_clean()


@pytest.mark.django_db
class TestProfileMode:
    @pytest.fixture
    @mute_signals(signals.post_save)
    def profile(self):
        user = UserFactory.create()
        return ProfileFactory.create(user=user)

    @mute_signals(signals.post_save)
    def custom_profile(self, *args, **kwargs):
        user = UserFactory.create()
        return ProfileFactory.build(user=user, *args, **kwargs)

    def test_str_profile(self, profile):
        assert str(profile) == profile.identificator

    def test_get_absolute_url(self, profile):
        expected_url = reverse(
            "profile", kwargs={"identificator": profile.identificator}
        )
        assert profile.get_absolute_url() == expected_url

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

    # def test_absolute_url(self, profile):
    #     excepted_url = reverse(
    #         "profile", kwargs={"identificator": profile.identificator}
    #     )
    #     assert profile.get_absolute_url() == excepted_url  # type: ignore


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
        user = get_user_model()
        instance = user(**user_data)
        assert instance.username == "Robert"  # type: ignore

    def test_user_data_password(self, user_data):
        user = get_user_model()
        instance = user(**user_data)
        assert instance.password == "robert123"


# TODO: MOVE TO GLOBAL TESTS????
@pytest.mark.no_cover
def test_debug_toolbar():
    if settings.DEBUG:
        client = Client()
        response = client.get(reverse("debug_toolbar:debug_toolbar"))
        assert response.status_code == 200
    else:
        assert True
