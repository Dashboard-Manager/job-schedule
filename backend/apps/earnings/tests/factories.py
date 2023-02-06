from apps.earnings.models import Earnings
from apps.users.tests.factories import ProfileFactory
from factory import LazyFunction, SubFactory
from factory.django import DjangoModelFactory
from faker import Faker
from faker.providers import python

faker = Faker()
faker.add_provider(python)


class EarningsFactory(DjangoModelFactory):
    class Meta:
        model = Earnings

    constant_pension_contribution = LazyFunction(
        lambda: faker.pydecimal(left_digit=1, right_digit=2, positive=True)
    )
    constant_disability_contribution = LazyFunction(
        lambda: faker.pydecimal(left_digit=1, right_digit=2, positive=True)
    )

    constant_sickness_contribution = LazyFunction(
        lambda: faker.pydecimal(left_digit=1, right_digit=2, positive=True)
    )

    constant_health_care_contribution = LazyFunction(
        lambda: faker.pydecimal(left_digit=1, right_digit=2, positive=True)
    )

    constant_PIT = LazyFunction(
        lambda: faker.pydecimal(left_digit=1, right_digit=2, positive=True)
    )

    user = LazyFunction(lambda: SubFactory(ProfileFactory))
