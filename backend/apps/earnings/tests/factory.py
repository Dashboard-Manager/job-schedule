from datetime import timedelta

from apps.earnings.models import Calculations, Constants, JobHours, Settlements
from apps.users.tests.factory import ProfileFactory
from django.utils import timezone
from factory import LazyAttribute, LazyFunction, SubFactory
from factory.django import DjangoModelFactory
from faker import Faker
from faker.providers import date_time, internet, python

faker = Faker()
faker.add_provider(internet)
faker.add_provider(date_time)
faker.add_provider(python)


class ConstantsFactory(DjangoModelFactory):
    class Meta:
        model = Constants

    PIT = LazyFunction(
        lambda: faker.pydecimal(left_digit=2, right_digit=2, positive=True)
    )
    pension_contribution = LazyFunction(
        lambda: faker.pydecimal(left_digit=1, right_digit=2, positive=True)
    )
    disability_contribution = LazyFunction(
        lambda: faker.pydecimal(left_digit=1, right_digit=2, positive=True)
    )

    sickness_contribution = LazyFunction(
        lambda: faker.pydecimal(left_digit=1, right_digit=2, positive=True)
    )

    health_care_contribution = LazyFunction(
        lambda: faker.pydecimal(left_digit=1, right_digit=2, positive=True)
    )
    user = LazyFunction(lambda: SubFactory(ProfileFactory))


class CalculationsFactory(DjangoModelFactory):
    class Meta:
        model = Calculations

    pension_contribution = LazyFunction(
        lambda: faker.pydecimal(left_digit=1, right_digit=2, positive=True)
    )
    disability_contribution = LazyFunction(
        lambda: faker.pydecimal(left_digit=1, right_digit=2, positive=True)
    )

    sickness_contribution = LazyFunction(
        lambda: faker.pydecimal(left_digit=1, right_digit=2, positive=True)
    )

    health_care_contribution = LazyFunction(
        lambda: faker.pydecimal(left_digit=1, right_digit=2, positive=True)
    )
    income = LazyFunction(
        lambda: faker.pydecimal(left_digit=1, right_digit=2, positive=True)
    )
    income_tax = LazyFunction(
        lambda: faker.pydecimal(left_digit=1, right_digit=2, positive=True)
    )
    netto_salary = LazyFunction(
        lambda: faker.pydecimal(left_digit=1, right_digit=2, positive=True)
    )

    constants = LazyFunction(lambda: SubFactory(ConstantsFactory))
    hours = LazyFunction(lambda: SubFactory)


class SettlementsFactory(DjangoModelFactory):
    class Meta:
        model = Settlements

    user = LazyFunction(lambda: SubFactory(ProfileFactory))
    date = LazyFunction(lambda: timezone.now())
    calculations = LazyFunction(lambda: SubFactory(CalculationsFactory))


class JobHoursFactory(DjangoModelFactory):
    class Meta:
        model = JobHours

    date = LazyFunction(lambda: timezone.now())
    user = SubFactory(ProfileFactory)
    start_date = LazyFunction(lambda: faker.date_object())
    end_date = LazyAttribute(
        lambda instance: instance.start_date + timedelta(days=faker.random_int(min=0))
    )
    hours = LazyFunction(lambda: faker.random_int(min=0))
    extra_hours = LazyFunction(lambda: faker.random_int(min=0))
