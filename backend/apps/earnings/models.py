import logging

from apps.earnings.services import constants
from apps.earnings.services.working_hours import get_working_hours
from apps.users.models import Profile
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
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

    user = models.OneToOneField("apps.users.models.Profile", on_delete=models.CASCADE)
    calculations = models.OneToOneField(
        "apps.earnings.models.Calculations", on_delete=models.CASCADE
    )


class Constants(models.Models):
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


class Calculations(models.Models):
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

    constants = models.OneToOneField(Constants, on_delete=models.CASCADE)
    hours = models.OneToOneField(
        "apps.earnings.models.JobHours", on_delete=models.CASCADE
    )

    @property
    def brutto_salary(self) -> float:
        # return self.salary.brutto
        if self.hours.extra_hours:
            return (self.hours.hours * self.user.hours_brutto_salary) + (
                self.hours.extra_hours * self.user.extra_hours_brutto_salary
            )
        return self.hours.hours * self.user.hours_brutto_salary

    @property
    def netto_salary(self) -> float:
        self.netto_salary = round(
            (
                self.brutto_salary
                - self.constants.ZUS_contributions
                - self.health_care_contribution
                - self.income_tax
            ),
            2,
        )
        return self.netto_salary


class JobHours(BaseModel):
    date = models.DateField(default=timezone.now)
    start_date = models.TimeField(default=timezone.now)
    end_date = models.TimeField(default=timezone.now)
    hours = models.PositiveSmallIntegerField(
        default=0,
        validators=[
            MinValueValidator(
                limit_value=0,
                message="Working hours cannot be less than 0",
            ),
            MaxValueValidator(
                limit_value=24,
                message="Working hours cannot be more than 24h. Day has 24h.",
            ),
        ],
    )

    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return f"{self.user} has {self.hours} hours in date"

    def save(self, *args, **kwargs):
        self.hours = get_working_hours(self.user, self.start_date, self.end_date)
        self.extra_hours = get_working_hours(
            self.user, self.start_date, self.end_date, extra_hours=True
        )
        super(JobHours, self).save(*args, **kwargs)

    def clean(self):
        super().clean()
        if self.start_date > self.end_date:
            raise ValidationError("End date must be after start date")


# clean
