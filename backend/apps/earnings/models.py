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
from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class Earnings(BaseModel):

    constant_pension_contribution = models.FloatField(
        verbose_name="Constant Pension Contribution",
        default=constants.PENSION,
    )

    constant_disability_contribution = models.FloatField(
        verbose_name="Constant  Disability Contribution",
        default=constants.DISABILITY,
    )

    constant_sickness_contribution = models.FloatField(
        verbose_name="Constant Sickness Contribution",
        default=constants.SICKNESS,
    )

    constant_health_care_contribution = models.FloatField(
        verbose_name="Constant Health Care Contribution",
        default=constants.HEALTH_CARE,
    )

    constant_PIT = models.FloatField(
        verbose_name="Constant PIT tax",
        default=constants.PIT,
    )

    calculated_pension_contribution = models.FloatField(
        verbose_name="Calculated Pension Contribution", default=0
    )

    calculated_disability_contribution = models.FloatField(
        verbose_name="Calculated  Disability Contribution", default=0
    )

    calculated_sickness_contribution = models.FloatField(
        verbose_name="Calculated Sickness Contribution", default=0
    )

    calculated_health_care_contribution = models.FloatField(
        verbose_name="Calculated Health Care Contribution", default=0
    )

    calculated_PIT_tax = models.FloatField(verbose_name="Calculated PIT tax", default=0)

    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    @property
    def age(self) -> int:
        return self.user.age

    @property
    def brutto_salary(self) -> float:
        return self.user.salary

    def set_pension_contribution(self):
        self.calculated_pension_contribution = calc_pension_contr(
            self.brutto_salary,
            self.constant_pension_contribution,
        )
        self.save()

    def set_disability_contribution(self) -> float:
        return float(
            calc_disability_contr(
                self.brutto_salary,
                self.constant_disability_contribution,
            )
        )

    def set_sickness_contribution(self) -> float:
        return float(
            calc_sickness_contr(
                self.brutto_salary,
                self.constant_sickness_contribution,
            )
        )

    def set_ZUS_contributions(self) -> float:
        return round(
            (
                self.pension_contribution
                + self.disability_contribution
                + self.sickness_contribution
            ),
            2,
        )

    def set_health_care_contribution(self) -> float:
        return float(
            calc_health_care_contr(
                self.brutto_salary,
                self.ZUS_contributions,
                self.constant_health_care_contribution,
            )
        )

    def set_income(self) -> float:
        return float(
            calc_income(
                self.brutto_salary,
                self.ZUS_contributions,
            )
        )

    def set_income_tax(self) -> int:
        if self.user.age > 26:
            return int(
                calc_income_tax(
                    self.income,
                    int(self.constant_PIT),
                )
            )
        return 0

    def set_netto_salary(self) -> float:
        return round(
            (
                self.brutto_salary
                - self.ZUS_contributions
                - self.health_care_contribution
                - self.income_tax
            ),
            2,
        )


class JobHours(BaseModel):
    date = models.DateField(default=timezone.now)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)

    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return f"{self.user} has {self.hours} hours in job"

    @property
    def hours(self) -> int:
        if self.user:
            return int(
                get_working_hours(
                    self.user,
                    self.start_date,
                    self.end_date,
                )
            )
        return 0


# clean
