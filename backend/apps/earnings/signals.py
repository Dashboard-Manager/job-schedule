from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from apps.earnings.models import Calculations, JobHours
from apps.earnings.services.calculations import (
    calc_disability_contr,
    calc_health_care_contr,
    calc_income,
    calc_income_tax,
    calc_pension_contr,
    calc_sickness_contr,
)
from apps.earnings.services.working_hours import get_working_hours


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


@receiver(post_save, sender=Calculations)
def set_netto_salary(sender, instance, **kwargs):
    instance.netto_salary = round(
        (
            instance.brutto_salary
            - instance.constants.ZUS_contributions
            - instance.health_care_contribution
            - instance.income_tax
        ),
        2,
    )


@receiver(pre_save, sender=JobHours)
def get_workings_hours(sender, instance, **kwargs):
    instance.hours = get_working_hours(
        instance.user, instance.start_date, instance.end_date
    )


@receiver(pre_save, sender=JobHours)
def get_extra_workings_hours(sender, instance, **kwargs):
    instance.extra_hours = get_working_hours(
        instance.user, instance.start_date, instance.end_date, extra_hours=True
    )
