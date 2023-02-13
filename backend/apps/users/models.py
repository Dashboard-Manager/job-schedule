import datetime

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone


class Profile(AbstractUser):
    salary = models.FloatField(
        verbose_name="brutto salary",
        default=0.0,
        validators=[
            MinValueValidator(
                limit_value=0,
                message="Salary cannot be less than 0",
            ),
            MaxValueValidator(
                limit_value=9_999_999_999,
                message="Sorry, but we need to have some limits",
            ),
        ],
    )
    hours_brutto_salary = models.FloatField(
        default=0,
        validators=[
            MinValueValidator(
                limit_value=0,
                message="Salary cannot be less than 0",
            ),
            MaxValueValidator(
                limit_value=9_999_999_999,
                message="Sorry, but we need to have some limits",
            ),
        ],
    )
    extra_hours_brutto_salary = models.FloatField(
        default=0,
        validators=[
            MinValueValidator(
                limit_value=0,
                message="Salary cannot be less than 0",
            ),
            MaxValueValidator(
                limit_value=9_999_999_999,
                message="Sorry, but we need to have some limits",
            ),
        ],
    )
    birth_date = models.DateField(verbose_name="date of birth", blank=False, null=True)

    def __str__(self) -> str:
        return f"{self.username}"

    @property
    def age(self) -> int:
        if self.birth_date:
            return int(timezone.now().year - self.birth_date.year)
        return 0

    def get_absolute_url(self) -> str:
        return f"profile/{self.username}/"

    def clean(self, *args, **kwargs):
        super(Profile, self).clean(*args, **kwargs)
        if self.birth_date > datetime.date.today():
            raise ValidationError(
                {"birth_date": "The birth date cannot be in the past.."}
            )
        if self.age < 16:
            raise ValidationError({"age": "You are too young to use this application."})
