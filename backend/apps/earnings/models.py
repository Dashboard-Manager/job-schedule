import logging

from apps.earnings.services import constants
from apps.users.models import Profile
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone

logger = logging.getLogger(__name__)


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class Settlements(BaseModel):
    date = models.DateField(default=timezone.now)

    user = models.OneToOneField("users.Profile", on_delete=models.CASCADE)
    calculations = models.OneToOneField(
        "earnings.Calculations", on_delete=models.CASCADE
    )


class Constants(models.Model):
    PIT = models.FloatField(
        verbose_name="Constant PIT tax",
        default=constants.PIT,
    )

    pension_contribution = models.FloatField(
        verbose_name="Constant Pension Contribution",
        default=constants.PENSION,
    )

    disability_contribution = models.FloatField(
        verbose_name="Constant  Disability Contribution",
        default=constants.DISABILITY,
    )

    sickness_contribution = models.FloatField(
        verbose_name="Constant Sickness Contribution",
        default=constants.SICKNESS,
    )

    health_care_contribution = models.FloatField(
        verbose_name="Constant Health Care Contribution",
        default=constants.HEALTH_CARE,
    )

    user = models.ForeignKey("users.Profile", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Constants for {self.user}"

    @property
    def ZUS_contributions(self) -> float:
        return round(
            (
                self.pension_contribution
                + self.disability_contribution
                + self.sickness_contribution
            ),
            2,
        )


class Calculations(models.Model):
    pension_contribution = models.FloatField(
        verbose_name="Pension Contribution", default=0
    )
    disability_contribution = models.FloatField(
        verbose_name=" Disability Contribution", default=0
    )
    sickness_contribution = models.FloatField(
        verbose_name="Sickness Contribution", default=0
    )
    health_care_contribution = models.FloatField(
        verbose_name="Health Care Contribution", default=0
    )
    income = models.FloatField(verbose_name="Income", default=0)
    income_tax = models.FloatField(verbose_name="Income tax", default=0)
    netto_salary = models.FloatField(default=0)

    constants = models.OneToOneField(Constants, on_delete=models.CASCADE)
    hours = models.OneToOneField("earnings.JobHours", on_delete=models.CASCADE)
    user = models.ForeignKey("users.Profile", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user} earned {self.netto_salary} PLN"

    @property
    def brutto_salary(self) -> float:
        if self.user.salary > 0:
            return self.user.salary

        if self.hours.extra_hours:
            return (self.hours.hours * self.user.hours_brutto_salary) + (
                self.hours.extra_hours * self.user.extra_hours_brutto_salary
            )
        return self.hours.hours * self.user.hours_brutto_salary


class JobHours(BaseModel):
    date = models.DateField(default=timezone.now)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    hours = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(
                limit_value=0,
                message="Working hours cannot be less than 0",
            ),
        ],
    )
    extra_hours = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(
                limit_value=0,
                message="Working hours cannot be less than 0",
            ),
        ],
    )

    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return f"{self.user} has {self.hours} hours in date"

    def clean(self, *args, **kwargs):
        if self.start_date > self.end_date:
            raise ValidationError("End date must be after start date")
        super(JobHours, self).clean(*args, **kwargs)


# clean
