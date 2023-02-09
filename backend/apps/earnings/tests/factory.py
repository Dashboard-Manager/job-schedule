from apps.users.tests.factories import ProfileFactory
from django.utils import timezone
from factory import LazyFunction, SubFactory
from factory.django import DjangoModelFactory
from faker import Faker
from faker.providers import date_time, internet

faker = Faker()
faker.add_providers(internet)
faker.add_providers(date_time)


class ConstantsFactory(DjangoModelFactory):
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
    user = LazyFunction(lambda: SubFactory(ProfileFactory))
    date = LazyFunction(lambda: timezone.now())
    calculations = LazyFunction(lambda: SubFactory(CalculationsFactory))


class JobHoursFactory(DjangoModelFactory):
    date = LazyFunction(lambda: timezone.now())
    user = LazyFunction(lambda: SubFactory(ProfileFactory))
    start_date = LazyFunction(lambda: faker.date())
    end_date = LazyFunction(lambda: faker.date())
    hours = LazyFunction(lambda: faker.random_int(min=0))
    extra_hours = LazyFunction(lambda: faker.random_int(min=0))
