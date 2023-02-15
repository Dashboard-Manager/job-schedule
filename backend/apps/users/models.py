import datetime
from random import choice
from string import digits

from apps.earnings.services import constants
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    identificator = models.CharField(
        _("User identificator"), max_length=6, unique=True, editable=False
    )
    birth_date = models.DateField(
        verbose_name=_("Birth date"),
        blank=False,
        default=(timezone.now() - datetime.timedelta(days=16 * 365)),
    )
    user = models.OneToOneField(
        User, verbose_name=_("User"), on_delete=models.CASCADE, related_name="profile"
    )

    def __str__(self) -> str:
        return f"{self.identificator}"

    def save(self, *args, **kwargs):
        if not self.identificator:
            self.identificator = self.id_generator()
            while Profile.objects.filter(identificator=self.identificator).exists():
                self.identificator = self.id_generator()
        super(Profile, self).save(*args, **kwargs)

    @property
    def age(self) -> int:
        if self.birth_date:
            return int(timezone.now().year - self.birth_date.year)
        return 0

    def id_generator(self, size: int = 6, chars: str = digits):
        return "".join(choice(chars) for _ in range(size))

    def clean(self, *args, **kwargs):
        super(Profile, self).clean(*args, **kwargs)
        if self.birth_date and self.birth_date > datetime.date.today():
            raise ValidationError(
                {"error": _("The birth date cannot be in the past..")}
            )
        if self.age < 16:
            raise ValidationError(
                {"error": _("You are too young to use this application.")}
            )


class Financials(models.Model):
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
    student = models.BooleanField(verbose_name=_("Student status"), default=False)

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
        default=0.0,
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
        default=0.0,
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
        default=0.0,
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

    user = models.OneToOneField(
        User,
        verbose_name=_("user"),
        on_delete=models.CASCADE,
        related_name="financials",
    )

    def __str__(self) -> str:
        return f"{self.user.profile.identificator}"

    def clean(self, *args, **kwargs):
        # xxx
        super(Financials, self).clean(*args, **kwargs)
