import logging

from apps.users.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from apps.earnings.services import constants

logger = logging.getLogger(__name__)


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class Settlements(BaseModel):
    class Meta:
        verbose_name = "settlements"
        verbose_name_plural = "1. Settlements"

    date = models.DateField(default=timezone.now)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    calculations = models.OneToOneField(
        "earnings.Calculations", on_delete=models.CASCADE
    )


class Constants(models.Model):
    class Meta:
        verbose_name = "constants"
        verbose_name_plural = "3. Constants for calculations"

    date = models.DateField(_("Constant at date"), auto_now=True)  # noqa

    PIT = models.FloatField(
        verbose_name=_("Constant PIT tax"),
        default=constants.PIT,
    )

    pension_contribution = models.FloatField(
        verbose_name=_("Pension Contribution"),
        default=constants.PENSION,
    )

    disability_contribution = models.FloatField(
        verbose_name=_("Disability Contribution"),
        default=constants.DISABILITY,
    )

    sickness_contribution = models.FloatField(
        verbose_name=_("Sickness Contribution"),
        default=constants.SICKNESS,
    )

    health_care_contribution = models.FloatField(
        verbose_name=_("Health Care Contribution"),
        default=constants.HEALTH_CARE,
    )

    def __str__(self) -> str:
        return f"Constants at {self.date}"


class Calculations(models.Model):
    class Meta:
        verbose_name = "calculations"
        verbose_name_plural = "2. Financial calculations"

    pension_contribution = models.FloatField(
        verbose_name=_("Pension Contribution"), default=0.0
    )
    disability_contribution = models.FloatField(
        verbose_name=_("Disability Contribution"), default=0.0
    )
    sickness_contribution = models.FloatField(
        verbose_name=_("Sickness Contribution"), default=0.0
    )
    health_care_contribution = models.FloatField(
        verbose_name=_("Health Care Contribution"), default=0.0
    )
    income = models.FloatField(
        verbose_name=_("Income"),
        help_text=_(
            "Dopóki twoje burtto zarobek nie przekracza kosztów przychodu wynosi 0"
        ),
        default=0.0,
    )
    income_tax = models.FloatField(
        verbose_name=_("Income tax"),
        help_text=_(
            "Dopóki twoje burtto zarobek nie przekracza kosztów przychodu wynosi 0"
        ),
        default=0.0,
    )
    netto_salary = models.FloatField(verbose_name=_("Netto salary"), default=0)

    constants = models.OneToOneField(Constants, on_delete=models.CASCADE)
    hours = models.OneToOneField("earnings.JobHours", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user} earned {self.netto_salary} PLN"

    @property
    def brutto_salary(self) -> float:
        profile_financials = self.user.profile.financials  # type: ignore
        hourly_pay = profile_financials.hourly_pay
        extra_hourly_pay = profile_financials.extra_hourly_pay
        extra_hours = self.hours.extra_hours
        calc = (self.hours.hours * hourly_pay) + (
            self.hours.extra_hours * extra_hourly_pay
        )
        if profile_financials.salary > 0:
            return profile_financials.salary

        return calc if extra_hours else self.hours.hours * hourly_pay


class JobHours(BaseModel):
    class Meta:
        verbose_name = "job hours"
        verbose_name_plural = "4. Your job hours"

    date = models.DateField(default=timezone.now)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    hours = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(
                limit_value=0,
                message=_("Working hours cannot be less than 0"),
            ),
        ],
    )
    extra_hours = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(
                limit_value=0,
                message=_("Working hours cannot be less than 0"),
            ),
        ],
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return f"{self.user} has {self.hours} hours and {self.extra_hours} extra hours"

    def clean(self, *args, **kwargs):
        if self.start_date > self.end_date:
            raise ValidationError(_("End date must be after start date"))
        super(JobHours, self).clean(*args, **kwargs)


# clean
