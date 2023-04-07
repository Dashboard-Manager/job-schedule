from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
import datetime


def validate_age(value):
    if int(timezone.now().year - value.year) < 16:
        raise ValidationError(
            {"error": _("You are too young to use this application.")}
        )


def validate_future_date(value):
    if value > datetime.date.today():
        raise ValidationError({"error": _("The birth date cannot be in the future..")})
