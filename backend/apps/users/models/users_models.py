from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.urls import reverse
from django.core.exceptions import ValidationError
import uuid
from apps.users.managers import UserManager
from apps.users.validations import validate_age, validate_future_date


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        _("email address"),
        unique=True,
    )
    first_name = models.CharField(
        _("first name"),
        max_length=150,
        blank=True,
    )
    last_name = models.CharField(
        _("last name"),
        max_length=150,
        blank=True,
    )
    birth_date = models.DateField(
        verbose_name=_("Birth date"),
        blank=False,
        validators=[
            validate_age,
            validate_future_date,
        ],
    )
    is_staff = models.BooleanField(
        default=False,
    )
    is_active = models.BooleanField(
        default=True,
    )
    date_joined = models.DateTimeField(
        default=timezone.now,
    )
    is_chief = models.BooleanField(
        default=False,
    )
    is_team_leader = models.BooleanField(
        default=False,
    )
    is_accountant = models.BooleanField(
        default=False,
    )
    is_employee = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "birth_date"]

    objects = UserManager()

    def __str__(self) -> str:
        return self.email


class User(CustomUser):
    ROLE_CHOICES = [
        ("chief", "Chief"),
        ("team leader", "Team Leader"),
        ("accountant", "Accountant"),
        ("employee", "Employee"),
    ]

    identificator = models.UUIDField(
        verbose_name=_("User identificator"),
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )

    username_id = models.CharField(
        verbose_name=_("Username id"),
        max_length=8,
        unique=True,
        editable=False,
    )

    username = None

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, editable=False)

    def clean_username_id(self) -> None:
        """user function to set username id number"""
        if User.objects.exists():
            user = User.objects.last()
            if user:
                self.username_id = str(int(user.username_id) + 1)
        else:
            if not self.username_id:
                self.username_id = "00000000"

    def clean_username(self) -> None:
        """user function create username field from firstname and lastname

        Raises:
            ValidationError: You must fill both first and last names
        """
        if all([self.first_name, self.last_name, self.username_id]):
            self.username = f"{self.first_name}{self.last_name}#{self.username_id}"
        else:
            raise ValidationError(
                {"error": _("You must fill both first and last names")}
            )

    @property
    def age(self) -> int:
        return int(timezone.now().year - self.birth_date.year)

    @classmethod
    def select_active_role(cls) -> None:
        """function to pass the role to the user"""
        if cls.role == "chief":
            cls.is_chief = True
        elif cls.role == "team leader":
            cls.is_team_leader = True
        elif cls.role == "accountant":
            cls.is_accountant = True
        elif cls.role == "employee":
            cls.is_employee = True

    def save(self, *args, **kwargs):
        self.select_active_role()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("users", kwargs={"identificator": self.identificator})


class UserChief(User):
    pass


class UserTeamLeader(User):
    pass


class UserAccountant(User):
    pass


class UserEmployee(User):
    pass
