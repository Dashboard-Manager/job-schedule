import datetime

from apps.schedules.models import Job
from apps.users.tests.factory import UserFactory
from factory import LazyAttribute, LazyFunction, SubFactory
from factory.django import DjangoModelFactory
from faker import Faker
from faker.providers import date_time

faker = Faker()
faker.add_provider(date_time)


class JobFactory(DjangoModelFactory):
    class Meta:
        model = Job

    date = LazyFunction(lambda: faker.date_object())
    start_job = LazyAttribute(
        lambda instance: instance.date
        + datetime.timedelta(hours=faker.random_int(min=0, max=12))
    )
    end_job = LazyAttribute(
        lambda instance: instance.date
        + datetime.timedelta(hours=faker.random_int(min=12, max=23))
    )
    hours = LazyFunction(lambda: faker.random_int(min=0, max=24))
    extra_hours = LazyFunction(lambda: faker.random_int(min=0, max=24))
    user = SubFactory(UserFactory)

    created_at = LazyFunction(lambda: faker.date_time())
    updated_at = LazyAttribute(
        lambda instance: instance.created_at + datetime.timedelta(minutes=1)
    )
