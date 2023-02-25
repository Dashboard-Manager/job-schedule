from factory import LazyFunction, SubFactory
from factory.django import DjangoModelFactory
from apps.schedules.models import Task
from apps.users.tests.factory import ProfileFactory
from faker import Faker
from faker.providers import date_time, internet, python

faker = Faker()
faker.add_provider(internet)
faker.add_provider(date_time)
faker.add_provider(python)
faker.seed(0)


class TaskFactory(DjangoModelFactory):
    class Meta:
        model = Task

    title = LazyFunction(lambda: faker.sentence(nb_words=5))
    description = LazyFunction(lambda: faker.sentence(nb_words=100))
    priority = 'medium'
    created_by = SubFactory(ProfileFactory)
    assigned_user = SubFactory(ProfileFactory)
