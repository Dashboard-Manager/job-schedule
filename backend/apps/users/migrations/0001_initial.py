# Generated by Django 4.1.7 on 2023-03-03 18:51

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "identificator",
                    models.CharField(
                        editable=False,
                        max_length=6,
                        unique=True,
                        verbose_name="User identificator",
                    ),
                ),
                (
                    "birth_date",
                    models.DateField(
                        default=django.utils.timezone.now, verbose_name="Birth date"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "verbose_name": "user profile",
                "verbose_name_plural": "User profiles",
            },
        ),
        migrations.CreateModel(
            name="Financials",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "contract",
                    models.CharField(
                        choices=[
                            ("employment", "Employment contract"),
                            ("commission", "Commission contract"),
                            ("specific-task", "Specific-task contract"),
                            (
                                "commission with economic entity",
                                "Commission contract with an economic entity",
                            ),
                            (
                                "intership",
                                "Student and postgraduate internship contract",
                            ),
                        ],
                        default="employment",
                        max_length=50,
                        verbose_name="Type of contract",
                    ),
                ),
                (
                    "is_student",
                    models.BooleanField(default=False, verbose_name="Student status"),
                ),
                (
                    "work_in_the_place_of_residence",
                    models.BooleanField(
                        default=True, verbose_name="Work in the place of residence"
                    ),
                ),
                (
                    "voluntary_health_insurance",
                    models.BooleanField(
                        default=True, verbose_name="Volunatry health insurance"
                    ),
                ),
                (
                    "health_insurance",
                    models.FloatField(
                        default=2.45, verbose_name="Value of health insurance"
                    ),
                ),
                (
                    "joint_taxation_of_spouses",
                    models.BooleanField(
                        default=False, verbose_name="Joint taxation of spouses"
                    ),
                ),
                (
                    "have_extra_salary",
                    models.BooleanField(
                        default=True,
                        verbose_name="Have you extra salary for over time?",
                    ),
                ),
                (
                    "salary",
                    models.FloatField(
                        default=0,
                        validators=[
                            django.core.validators.MinValueValidator(
                                limit_value=0, message="Salary cannot be less than 0"
                            ),
                            django.core.validators.MaxValueValidator(
                                limit_value=9999999999,
                                message="Sorry, but we need to have some limits",
                            ),
                        ],
                        verbose_name="Brutto salary",
                    ),
                ),
                (
                    "hourly_pay",
                    models.FloatField(
                        default=0,
                        validators=[
                            django.core.validators.MinValueValidator(
                                limit_value=0, message="Salary cannot be less than 0"
                            ),
                            django.core.validators.MaxValueValidator(
                                limit_value=9999999999,
                                message="Sorry, but we need to have some limits",
                            ),
                        ],
                        verbose_name="Hourly brutto pay",
                    ),
                ),
                (
                    "extra_hourly_pay",
                    models.FloatField(
                        default=0,
                        help_text="Extra pay for overtime",
                        validators=[
                            django.core.validators.MinValueValidator(
                                limit_value=0, message="Salary cannot be less than 0"
                            ),
                            django.core.validators.MaxValueValidator(
                                limit_value=9999999999,
                                message="Sorry, but we need to have some limits",
                            ),
                        ],
                        verbose_name="Hourly extra brutto pay",
                    ),
                ),
                (
                    "profile",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="financials",
                        to="users.profile",
                        verbose_name="User profile",
                    ),
                ),
            ],
            options={
                "verbose_name": "financial profile",
                "verbose_name_plural": "Financial profiles",
            },
        ),
    ]
