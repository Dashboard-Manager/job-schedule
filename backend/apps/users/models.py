from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class Profile(AbstractUser):
    salary = models.FloatField(verbose_name="brutto salary", default=0.0)
    birth_date = models.DateField(verbose_name="date of birth", blank=True, null=True)

    @property
    def age(self) -> int:
        if self.birth_date:
            return int(timezone.now().year - self.birth_date.year)
        return 0
