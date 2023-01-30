from apps.users.models import Profile
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):  # type: ignore
    class Meta:
        abstract = True

    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class Event(BaseModel):
    # choices
    class TypeOfEvent(models.TextChoices):  # type: ignore
        TASK = "TASK", _("Task")
        JOB = "JOB", _("Job hours")
        EVENT = "EVENT", _("Job event")

    title = models.TextField(
        verbose_name="Title of event",
        default="title",
    )
    description = models.TextField(
        verbose_name="Description of event",
        default="...",
    )
    type = models.CharField(
        max_lentgh=5,
        choices=TypeOfEvent.choices,
        default=TypeOfEvent.JOB,
    )

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    from_user = models.ForeignKey(
        Profile,
        verbose_name="Event author",
        blank=True,
        null=True,
        related_name="author",
    )
    to_user = models.ForeignKey(
        Profile,
        verbose_name="Event performer",
        blank=True,
        null=True,
        related_name="performer",
    )

    # slug = models.SlugField(max_length=50, )

    # TODO: create validators
    # TODO: slug filed?
