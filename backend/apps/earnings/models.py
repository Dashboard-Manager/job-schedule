from apps.earnings.services import constants
from apps.earnings.services.working_hours import get_working_hours
from apps.users.models import Profile
from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class Constants(BaseModel):
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


class Calculations(BaseModel):
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

    settlement = models.ForeignKey(
        "Settlements", on_delete=models.CASCADE, related_name="employer"
    )
    constants = models.ForeignKey(Constants, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.netto_salary = round(  # type: ignore
            (
                self.brutto_salary
                - self.constants.ZUS_contributions
                - self.health_care_contribution
                - self.income_tax
            ),
            2,
        )
        super(Calculations, self).save(*args, **kwargs)

    @property
    def brutto_salary(self) -> float:
        return self.settlement.user.salary


class JobHours(BaseModel):
    date = models.DateField(default=timezone.now)
    start_job = models.TimeField(auto_now_add=True, default=timezone.now())
    end_job = models.TimeField(default=timezone.now)
    hours = models.PositiveIntegerField(default=0)

    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return f"{self.user} has {self.hours} hours in job"

    def set_hours(self):
        self.hours = get_working_hours(
            self.user,
            self.start_job,
            self.end_job,
        )
        self.save()

    def clean(self):
        super().clean()
        if self.start_job > self.end_job:
            raise ValueError("End date must be after start date")


# clean
