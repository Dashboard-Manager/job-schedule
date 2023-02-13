from apps.users.models import Profile
from django.contrib.auth.hashers import make_password
from factory import LazyFunction
from factory.django import DjangoModelFactory
from faker import Faker
from faker.providers import date_time, internet, python

faker = Faker()
faker.add_provider(internet)
faker.add_provider(date_time)
faker.add_provider(python)


class ProfileFactory(DjangoModelFactory):
    class Meta:
        model = Profile

    username = LazyFunction(lambda: faker.user_name())
    password = LazyFunction(lambda: make_password(faker.password()))
    email = LazyFunction(lambda: faker.email())
    is_staff = False
    is_superuser = False

    salary = LazyFunction(
        lambda: faker.pyfloat(right_digits=2, min_value=0, max_value=9_999_999_999)
    )
    hourly_pay = LazyFunction(lambda: faker.random_int(min=0))
    extra_hourly_pay = LazyFunction(lambda: faker.random_int(min=0))

    birth_date = LazyFunction(lambda: faker.date_of_birth(minimum_age=18))
