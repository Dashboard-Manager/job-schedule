from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
from apps.earnings.services import constants
from apps.users.models import User


class Financials(models.Model):
    class Meta:
        verbose_name = "financial profile"
        verbose_name_plural = "Financial profiles"

    EMPLOYMENT = "employment"
    COMMISSION = "commission"
    SPECIFIC_TASK = "specific-task"
    COMMISSION_WITH_ECONOMIC_ENTITY = "commission with economic entity"
    INTERSHIP = "intership"
    CONTRACTS = [
        (EMPLOYMENT, _("Employment contract")),
        (COMMISSION, _("Commission contract")),
        (SPECIFIC_TASK, _("Specific-task contract")),
        (
            COMMISSION_WITH_ECONOMIC_ENTITY,
            _("Commission contract with an economic entity"),
        ),
        (INTERSHIP, _("Student and postgraduate internship contract")),
    ]
    contract = models.CharField(
        _("Type of contract"), choices=CONTRACTS, max_length=50, default=EMPLOYMENT
    )
    is_student = models.BooleanField(verbose_name=_("Student status"), default=False)

    work_in_the_place_of_residence = models.BooleanField(
        _("Work in the place of residence"), default=True
    )
    voluntary_health_insurance = models.BooleanField(
        _("Volunatry health insurance"), default=True
    )
    health_insurance = models.FloatField(
        verbose_name=_("Value of health insurance"), default=constants.SICKNESS
    )
    joint_taxation_of_spouses = models.BooleanField(
        _("Joint taxation of spouses"),
        default=False,
    )
    have_extra_salary = models.BooleanField(
        _("Have you extra salary for over time?"), default=True
    )

    salary = models.FloatField(
        verbose_name=_("Brutto salary"),
        default=0,
        validators=[
            MinValueValidator(
                limit_value=0,
                message=_("Salary cannot be less than 0"),
            ),
            MaxValueValidator(
                limit_value=9_999_999_999,
                message=_("Sorry, but we need to have some limits"),
            ),
        ],
    )

    hourly_pay = models.FloatField(
        verbose_name=_("Hourly brutto pay"),
        default=0,
        validators=[
            MinValueValidator(
                limit_value=0,
                message=_("Salary cannot be less than 0"),
            ),
            MaxValueValidator(
                limit_value=9_999_999_999,
                message=_("Sorry, but we need to have some limits"),
            ),
        ],
    )

    extra_hourly_pay = models.FloatField(
        verbose_name=_("Hourly extra brutto pay"),
        help_text=_("Extra pay for overtime"),
        default=0,
        validators=[
            MinValueValidator(
                limit_value=0,
                message=_("Salary cannot be less than 0"),
            ),
            MaxValueValidator(
                limit_value=9_999_999_999,
                message=_("Sorry, but we need to have some limits"),
            ),
        ],
    )

    profile = models.OneToOneField(
        User,
        verbose_name=_("User financial"),
        on_delete=models.CASCADE,
        related_name="financial",
    )

    def __str__(self) -> str:
        return f"{self.profile.identificator}"  # type: ignore
