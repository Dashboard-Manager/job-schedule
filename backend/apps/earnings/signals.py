from apps.earnings.models import Calculations
from apps.earnings.services.calculations import (
    calc_disability_contr,
    calc_health_care_contr,
    calc_income,
    calc_income_tax,
    calc_pension_contr,
    calc_sickness_contr,
)
from django.db.models.signals import pre_save
from django.dispatch import receiver


@receiver(pre_save, sender=Calculations)
def calculate_contributions(sender, instance, **kwargs):
    instance.pension_contribution = calc_pension_contr(
        instance.brutto_salary,
        instance.constants.pension_contribution,
    )
    instance.disability_contribution = calc_disability_contr(
        instance.brutto_salary,
        instance.constants.disability_contribution,
    )
    instance.sickness_contribution = calc_sickness_contr(
        instance.brutto_salary,
        instance.constants.sickness_contribution,
    )
    instance.health_care_contribution = calc_health_care_contr(
        instance.brutto_salary,
        instance.constants.ZUS_contributions,
        instance.constants.health_care_contribution,
    )
    instance.income = calc_income(
        instance.brutto_salary,
        instance.constants.ZUS_contributions,
    )
    if instance.user.age > 26:
        instance.income_tax = calc_income_tax(
            instance.income,
            instance.constants.PIT,
        )
    else:
        instance.income_tax = 0


# @receiver(pre_save, sender=Salaries)
# def set_salary(sender, instance, **kwargs):
#     netto = instance.calculations.netto_salary
#     instance.netto_salary = netto

#     # instance.brutto_salary = instance.calculations.brutto_salary
