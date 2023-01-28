from django.db import models
from django.utils import timezone
from services.calculations import (
    calc_disability_contr,
    calc_health_care_contr,
    calc_income,
    calc_income_tax,
    calc_pension_contr,
    calc_sickness_contr,
)


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class Earnings(BaseModel):
    user = models.ForeignKey("Profile")

    @property
    def brutto_salary(self) -> float:
        return self.user.salary

    @property
    def pension_contribution(self) -> float:
        return calc_pension_contr(self.brutto_salary)

    @property
    def disability_contribution(self) -> float:
        return calc_disability_contr(self.brutto_salary)

    @property
    def sickness_contribution(self) -> float:
        return calc_sickness_contr(self.brutto_salary)

    @property
    def ZUS_contributions(self) -> float:
        return (
            self.pension_contribution
            + self.disability_contribution
            + self.sickness_contribution
        )

    @property
    def health_care_contribution(self) -> float:
        return calc_health_care_contr(self.brutto_salary, self.ZUS_contributions)

    @property
    def income(self) -> float:
        return calc_income(self.brutto_salary, self.ZUS_contributions)

    @property
    def income_tax(self) -> int:
        return calc_income_tax(self.income)

    @property
    def netto_salary(self) -> float:
        if self.user.age > 26:
            return (
                self.brutto_salary
                - self.ZUS_contributions
                - self.health_care_contribution
                - self.income_tax
            )
        return (
            self.brutto_salary - self.ZUS_contributions - self.health_care_contribution
        )
