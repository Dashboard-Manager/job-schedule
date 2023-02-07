from apps.earnings.services import constants
from apps.earnings.services.calculations import (
    calc_disability_contr,
    calc_health_care_contr,
    calc_income,
    calc_income_tax,
    calc_pension_contr,
    calc_sickness_contr,
)
from apps.earnings.services.working_hours import get_working_hours
from apps.users.models import Profile
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
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

    settlement = models.ForeignKey(
        "Settlements", on_delete=models.CASCADE, related_name="employer"
    )
    constants = models.ForeignKey(Constants, on_delete=models.CASCADE)

    @property
    def brutto_salary(self) -> float:
        return self.settlement.user.salary

    @property
    def income(self) -> float:
        return calc_income(
            self.brutto_salary,
            self.constants.ZUS_contributions,
        )

    def set_contributions(self):
        self.pension_contribution = calc_pension_contr(
            self.brutto_salary,
            self.constants.pension_contribution,
        )
        self.disability_contribution = calc_disability_contr(
            self.brutto_salary,
            self.constants.disability_contribution,
        )
        self.sickness_contribution = calc_sickness_contr(
            self.brutto_salary,
            self.constants.sickness_contribution,
        )
        self.health_care_contribution = calc_health_care_contr(
            self.brutto_salary,
            self.constants.ZUS_contributions,
            self.constants.health_care_contribution,
        )
        self.save()

    def set_income_tax(self) -> int:
        if self.user.age > 26:
            self.income_tax = calc_income_tax(
                self.income,
                self.constants.PIT,
            )
            self.save()

    def set_netto_salary(self) -> float:
        self.netto_salary = round(
            (
                self.brutto_salary
                - self.constants.ZUS_contributions
                - self.health_care_contribution
                - self.income_tax
            ),
            2,
        )
        self.save()


class Salaries(BaseModel):
    brutto_salary = models.FloatField()
    netto_salary = models.FloatField()

    calculations = models.ForeignKey(Calculations, on_delete=models.CASCADE)

    def set_netto_salary(self):
        self.netto_salary = self.calculations.netto_salary
        self.save()

    def set_brutto_salary(self):
        self.brutto_salary = self.calculations.brutto_salary
        self.save()


class Settlements(BaseModel):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    constants = models.ForeignKey(
        Constants, on_delete=models.CASCADE, related_name="contributions"
    )
    calculations = models.OneToOneField(
        Calculations, on_delete=models.CASCADE, related_name="calculationed"
    )
    salary = models.ForeignKey(
        Salaries, on_delete=models.CASCADE, related_name="converted"
    )


class JobHours(BaseModel):
    date = models.DateField(default=timezone.now)
    start_job = models.TimeField(auto_now_add=True, default=timezone.now())
    end_job = models.TimeField(default=timezone.now)
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
            raise ValidationError("End date must be after start date")


# clean
