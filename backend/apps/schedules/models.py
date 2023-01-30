from apps.users.models import Profile
from django.db import models
from django.utils import timezone


class BaseModel(models.Model):  # type: ignore
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
        Profile,
        verbose_name="Event author",
        blank=True,
        null=True,
        related_name="author",
        on_delete=models.SET_NULL,
    )
    to_user = models.ForeignKey(
        Profile,
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

    user = models.ForeignKey(Profile, related_name="employer", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user} worked by {self.job_hours} hours"

    @property
    def job_hours(self) -> int:
        if self.end_job:
            return int(divmod((self.end_job - self.start_job).total_seconds(), 3600)[0])
        return 0


# TODO: class Task(BaseModel)... #noqa #type: ignore
