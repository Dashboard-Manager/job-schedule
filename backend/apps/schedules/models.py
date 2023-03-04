from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from apps.users.models import User


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class Event(BaseModel):
    title = models.TextField(
        verbose_name="Title of event",
        default="title",
    )
    description = models.TextField(
        verbose_name="Description of event",
        default="...",
    )

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    from_user = models.ForeignKey(
        User,
        verbose_name="Event author",
        blank=True,
        null=True,
        related_name="author",
        on_delete=models.SET_NULL,
    )
    to_user = models.ForeignKey(
        User,
        verbose_name="Event performer",
        blank=True,
        null=True,
        related_name="performer",
        on_delete=models.SET_NULL,
    )

    def __str__(self) -> str:
        return f"{self.title}"


class Job(BaseModel):
    date = models.DateField(default=timezone.now)

    start_job = models.DateTimeField(
        verbose_name="Start working", db_index=True, default=timezone.now
    )
    end_job = models.DateTimeField(verbose_name="Stop working", blank=True, null=True)

    hours = models.FloatField(_("Working hours"), default=0)  # <8
    extra_hours = models.FloatField(_("Working overtime hours"), default=0)  # >8

    user = models.ForeignKey(User, related_name="employer", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user} worked by {self.hours} and {self.extra_hours} hours"


# TODO: class Task(BaseModel)... #noqa #type: ignore
