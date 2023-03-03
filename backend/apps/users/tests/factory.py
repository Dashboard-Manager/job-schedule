from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from factory import LazyAttribute, LazyFunction, PostGenerationMethodCall, SubFactory
from factory.django import DjangoModelFactory
from faker import Faker
from faker.providers import date_time, internet, python

from apps.users.models import Profile

faker = Faker()
faker.add_provider(internet)
faker.add_provider(date_time)
faker.add_provider(python)

User = get_user_model()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = LazyFunction(lambda: faker.user_name())
    password = LazyFunction(lambda: make_password(faker.password()))
    email = LazyAttribute(lambda o: f"{o.username}@example.com")
    is_staff = False
    is_superuser = False


class ProfileFactory(DjangoModelFactory):
    class Meta:
        model = Profile

    identificator = PostGenerationMethodCall("id_generator")
    birth_date = LazyFunction(lambda: faker.date_of_birth(minimum_age=16))
    user = SubFactory(UserFactory)


class FinancialsFactory(DjangoModelFactory):
    class Meta:
        model = Financials

    profile = SubFactory(ProfileFactory)
    contract = LazyFunction(
        lambda: faker.random_element(elements=[x[0] for x in Financials.CONTRACTS])
    )
    is_student = LazyFunction(lambda: faker.boolean())
    work_in_the_place_of_residence = LazyFunction(lambda: faker.boolean())
    voluntary_health_insurance = LazyFunction(lambda: faker.boolean())
    health_insurance = LazyFunction(
        lambda: faker.pyfloat(right_digits=2, min_value=0, max_value=10)
    )
    joint_taxation_of_spouses = LazyFunction(lambda: faker.boolean())
    have_extra_salary = LazyFunction(lambda: faker.boolean())
    salary = LazyFunction(
        lambda: faker.pyfloat(right_digits=2, min_value=0, max_value=9_999_999_999)
    )
    hourly_pay = LazyFunction(lambda: faker.random_int(min=0))
    extra_hourly_pay = LazyFunction(lambda: faker.random_int(min=0))
