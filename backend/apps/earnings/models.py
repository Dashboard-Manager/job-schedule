from apps.earnings.services import constants
from apps.earnings.services.calculations import (
    calc_disability_contr,
    calc_health_care_contr,
    calc_income,
    calc_income_tax,
    calc_pension_contr,
    calc_sickness_contr,
)
from apps.users.models import Profile
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class BaseModel(models.Model):  # type: ignore
    class Meta:
        abstract = True

    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class Earnings(BaseModel):

    constant_pension_contribution = models.FloatField(
        verbose_name="Pension Contribution",
        default=constants.PENSION,
    )

    constant_disability_contribution = models.FloatField(
        verbose_name="Disability Contribution",
        default=constants.DISABILITY,
    )

    constant_sickness_contribution = models.FloatField(
        verbose_name="Sickness Contribution",
        default=constants.SICKNESS,
    )

    constant_health_care_contribution = models.FloatField(
        verbose_name="Health Care Contribution",
        default=constants.HEALTH_CARE,
    )

    constant_PIT = models.FloatField(
        verbose_name="PIT tax",
        default=constants.PIT,
    )

    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    @property
    def age(self) -> int:
        return int(self.user.age)

    @property
    def brutto_salary(self) -> float:
        return float(self.user.salary)

    @property
    def pension_contribution(self) -> float:
        return float(
            calc_pension_contr(
                self.brutto_salary,
                self.constant_pension_contribution,
            )
        )

    @property
    def disability_contribution(self) -> float:
        return float(
            calc_disability_contr(
                self.brutto_salary,
                self.constant_disability_contribution,
            )
        )

    @property
    def sickness_contribution(self) -> float:
        return float(
            calc_sickness_contr(
                self.brutto_salary,
                self.constant_sickness_contribution,
            )
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

    @property
    def health_care_contribution(self) -> float:
        return float(
            calc_health_care_contr(
                self.brutto_salary,
                self.ZUS_contributions,
                self.constant_health_care_contribution,
            )
        )

    @property
    def income(self) -> float:
        return float(
            calc_income(
                self.brutto_salary,
                self.ZUS_contributions,
            )
        )

    @property
    def income_tax(self) -> int:
        if self.user.age > 26:
            return int(
                calc_income_tax(
                    self.income,
                    self.constant_PIT,
                )
            )
        return 0

    @property
    def netto_salary(self) -> float:
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
    MONTH = "MONTHLY"
    WEEK = "WEEKLY"
    YEAR = "YEARLY"
    TIMEPERIOD = [
        (MONTH, _("Working hours from last month")),
        (WEEK, _("Working hours from last week")),
        (YEAR, _("Working hours from last week")),
    ]

    _job_hours = models.IntegerField(db_column="job_hours")
    date = models.DateField(default=timezone.now())

    period = models.CharField(choices=TIMEPERIOD, default=MONTH)

    def __str__(self) -> str:
        return f"{self.period} - {self.date}"

    @property
    def job_hours(self) -> int:
        return self._job_hours  # type: ignore

    @job_hours.setter
    def job_hours(self) -> None:
        if self.period == self.MONTHLY:
            self._job_hours = 1  # TODO: func to take hours from current month
        if self.period == self.WEEKLY:
            self._job_hours = 2  # TODO: func to take hours from current week
        if self.period == self.YEARLY:
            self._job_hours = 3  # TODO: func to take hours from current year
