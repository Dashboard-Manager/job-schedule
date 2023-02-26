import datetime

from apps.schedules.models import Job, Task
from apps.users.tests.factory import UserFactory
from factory import LazyAttribute, LazyFunction, SubFactory
from factory.django import DjangoModelFactory
from faker import Faker
from faker.providers import date_time

faker = Faker()
faker.add_provider(date_time)


class TaskFactory(DjangoModelFactory):
    class Meta:
        model = Task

    title = LazyFunction(lambda: faker.sentence(nb_words=5))
    description = LazyFunction(lambda: faker.sentence(nb_words=100))
    priority = LazyFunction(lambda: faker.random_element(elements=Task.PRIORITY_CHOICES)[0])
    created_by = SubFactory(UserFactory)
    assigned_user = SubFactory(UserFactory)


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
