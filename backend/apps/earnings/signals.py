from django.db.models.signals import pre_save
from django.dispatch import receiver

from apps.earnings.models import Calculations, JobHours
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


@receiver(pre_save, sender=Calculations)
def calculate_contributions(sender, instance, **kwargs):
    if not instance.user.profile.financials.is_student:
        instance.pension_contribution = calc_pension_contr(
            instance.brutto_salary,
            constants.PENSION,
        )
        instance.disability_contribution = calc_disability_contr(
            instance.brutto_salary,
            constants.DISABILITY,
        )
        if instance.user.profile.financials.voluntary_health_insurance:
            instance.sickness_contribution = calc_sickness_contr(
                instance.brutto_salary,
                instance.user.profile.financials.health_insurance,
            )
        else:
            instance.sickness_contribution = 0

        ZUS_contributions = round(
            (
                instance.pension_contribution
                + instance.disability_contribution
                + instance.sickness_contribution
            ),
            2,
        )

        instance.health_care_contribution = calc_health_care_contr(
            instance.brutto_salary,
            ZUS_contributions,
            constants.HEALTH_CARE,
        )

        instance.income = calc_income(
            instance.brutto_salary,
            ZUS_contributions,
        )

        instance.income_tax = calc_income_tax(
            instance.income,
            constants.PIT,
        )


@receiver(pre_save, sender=Calculations)
def set_netto_salary(sender, instance, **kwargs):
    ZUS_contributions = round(
        (
            instance.pension_contribution
            + instance.disability_contribution
            + instance.sickness_contribution
        ),
        2,
    )
    salary = round(
        (
            instance.brutto_salary
            - ZUS_contributions
            - instance.health_care_contribution
            - instance.income_tax
        ),
        2,
    )
    is_student = instance.user.profile.financials.is_student
    instance.netto_salary = salary if not is_student else instance.brutto_salary


@receiver(pre_save, sender=JobHours)
def get_workings_hours(sender, instance, **kwargs):
    hours = get_working_hours(instance.user, instance.start_date, instance.end_date)
    extra_hours = get_working_hours(
        instance.user, instance.start_date, instance.end_date, extra_hours=True
    )
    have_extra_salary = instance.user.profile.financials.have_extra_salary
    instance.hours = hours if have_extra_salary else hours + extra_hours
    instance.extra_hours = extra_hours if have_extra_salary else 0
