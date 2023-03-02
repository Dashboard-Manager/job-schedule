from datetime import timedelta

from django.utils import timezone
from factory import LazyAttribute, LazyFunction, SubFactory
from factory.django import DjangoModelFactory
from faker import Faker
from faker.providers import date_time, internet, python

from apps.earnings.models import Calculations, Constants, JobHours, Settlements
from apps.users.tests.factory import ProfileFactory, UserFactory

faker = Faker()
faker.add_provider(internet)
faker.add_provider(date_time)
faker.add_provider(python)


class JobHoursFactory(DjangoModelFactory):
    class Meta:
        model = JobHours

    date = LazyFunction(lambda: timezone.now())
    user = SubFactory(UserFactory)
    start_date = LazyFunction(lambda: faker.date_object())
    end_date = LazyAttribute(
        lambda instance: instance.start_date + timedelta(days=faker.random_int(min=0))
    )
    hours = LazyFunction(lambda: faker.random_int(min=0))
    extra_hours = LazyFunction(lambda: faker.random_int(min=0))


class ConstantsFactory(DjangoModelFactory):
    class Meta:
        model = Constants

    PIT = LazyFunction(lambda: faker.pydecimal(positive=True))
    pension_contribution = LazyFunction(lambda: faker.pydecimal(positive=True))
    disability_contribution = LazyFunction(lambda: faker.pydecimal(positive=True))

    sickness_contribution = LazyFunction(lambda: faker.pydecimal(positive=True))

    health_care_contribution = LazyFunction(lambda: faker.pydecimal(positive=True))
    date = LazyFunction(lambda: timezone.now())


class CalculationsFactory(DjangoModelFactory):
    class Meta:
        model = Calculations

    pension_contribution = LazyFunction(lambda: faker.random_int(min=0))
    disability_contribution = LazyFunction(lambda: faker.random_int(min=0))
    sickness_contribution = LazyFunction(lambda: faker.random_int(min=0))

    health_care_contribution = LazyFunction(lambda: faker.random_int(min=0))

    income = LazyFunction(lambda: faker.random_int(min=0))
    income_tax = LazyFunction(lambda: faker.random_int(min=0))

    netto_salary = LazyFunction(lambda: faker.random_int(min=0))

    constants = LazyFunction(lambda: SubFactory(ConstantsFactory))
    hours = SubFactory(JobHoursFactory)


class SettlementsFactory(DjangoModelFactory):
    class Meta:
        model = Settlements

    user = LazyFunction(lambda: SubFactory(UserFactory))
    date = LazyFunction(lambda: timezone.now())
    calculations = LazyFunction(lambda: SubFactory(CalculationsFactory))
