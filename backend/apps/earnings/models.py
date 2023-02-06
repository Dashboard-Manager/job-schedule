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


class Constants(BaseModel):
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
        verbose_name="Calculated Pension Contribution", default=0
    )

    disability_contribution = models.FloatField(
        verbose_name="Calculated  Disability Contribution", default=0
    )

    sickness_contribution = models.FloatField(
        verbose_name="Calculated Sickness Contribution", default=0
    )

    health_care_contribution = models.FloatField(
        verbose_name="Calculated Health Care Contribution", default=0
    )

    income = models.FloatField(verbose_name="Calculated income", default=0)

    income_tax = models.FloatField(verbose_name="Calculated income tax", default=0)

    user = models.ForeignKey("Settlements", on_delete=models.CASCADE)
    constants = models.ForeignKey(Constants, on_delete=models.CASCADE)

    @property
    def brutto_salary(self) -> float:
        return self.user.salary

    @property
    def income(self) -> float:
        return calc_income(
            self.brutto_salary,
            self.ZUS_contributions,
        )

    def set_pension_contribution(self):
        self.pension_contribution = calc_pension_contr(
            self.brutto_salary,
            self.constants.constant_pension_contribution,
        )
        self.save()

    def set_disability_contribution(self) -> float:
        self.disability_contribution = calc_disability_contr(
            self.brutto_salary,
            self.constants.constant_disability_contribution,
        )
        self.save()

    def set_sickness_contribution(self) -> float:
        self.sickness_contribution = calc_sickness_contr(
            self.brutto_salary,
            self.constants.constant_sickness_contribution,
        )
        self.save()

    def set_health_care_contribution(self) -> float:
        self.health_care_contribution = calc_health_care_contr(
            self.brutto_salary,
            self.constants.ZUS_contributions,
            self.constants.constant_health_care_contribution,
        )
        self.save()

    def set_income_tax(self) -> int:
        if self.user.age > 26:
            self.income_tax = calc_income_tax(
                self.income,
                self.constants.constant_PIT,
            )
            self.save()
            return
        self.income_tax = 0
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
        self.brutto_salary = self.calculations.user.salary
        self.save()


class Settlements(BaseModel):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    constants = models.ForeignKey(Constants, on_delete=models.CASCADE)
    calculations = models.OneToOneField(Calculations, on_delete=models.CASCADE)
    salary = models.ForeignKey(Salaries, on_delete=models.CASCADE)


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
