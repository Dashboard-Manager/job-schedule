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


class BaseModel(models.Model):  # type: ignore
    class Meta:
        abstract = True

    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class Earnings(BaseModel):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    @property
    def age(self) -> int:
        return int(self.user.age)

    @property
    def brutto_salary(self) -> float:
        return float(self.user.salary)

    @property
    def pension_contribution(self) -> float:
        return float(calc_pension_contr(self.brutto_salary))

    @property
    def disability_contribution(self) -> float:
        return float(calc_disability_contr(self.brutto_salary))

    @property
    def sickness_contribution(self) -> float:
        return float(calc_sickness_contr(self.brutto_salary))

    @property
    def ZUS_contributions(self) -> float:
        return float(
            (
                self.pension_contribution
                + self.disability_contribution
                + self.sickness_contribution
            )
        )

    @property
    def health_care_contribution(self) -> float:
        return float(calc_health_care_contr(self.brutto_salary, self.ZUS_contributions))

    @property
    def income(self) -> float:
        return float(calc_income(self.brutto_salary, self.ZUS_contributions))

    @property
    def income_tax(self) -> int:
        if self.user.age > 26:
            return int(calc_income_tax(self.income))
        return 0

    @property
    def netto_salary(self) -> float:
        return float(
            (
                self.brutto_salary
                - self.ZUS_contributions
                - self.health_care_contribution
                - self.income_tax
            )
        )
