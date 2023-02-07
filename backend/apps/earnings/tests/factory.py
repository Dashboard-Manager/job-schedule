from apps.users.tests.factories import ProfileFactory
from factory import LazyFunction, SubFactory
from factory.django import DjangoModelFactory
from faker import Faker
from faker.providers import internet

faker = Faker()
faker.add_providers(internet)


class ConstantsFactory(DjangoModelFactory):
    PIT = LazyFunction(
        lambda: faker.pydecimal(left_digit=1, right_digit=2, positive=True)
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


class CalculationsFactory(DjangoModelFactory):
    constants = LazyFunction(lambda: SubFactory(ConstantsFactory))


class SalariesFactory(DjangoModelFactory):
    brutto_salary = LazyFunction(lambda: faker.random_int())


class SettlementsFactory(DjangoModelFactory):
    user = LazyFunction(lambda: SubFactory(ProfileFactory))
    constants = LazyFunction(lambda: SubFactory(ConstantsFactory))
    calculations = LazyFunction(lambda: SubFactory(CalculationsFactory))
    salary = LazyFunction(lambda: SubFactory(SalariesFactory))