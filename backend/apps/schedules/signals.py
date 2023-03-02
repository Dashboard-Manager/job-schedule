from django.db.models.signals import pre_save
from django.dispatch import receiver

from apps.schedules.models import Job
from apps.schedules.services import get_extra_job_hours, get_job_hours


@receiver(pre_save, sender=Job)
def get_extra_workings_hours(sender, instance, **kwargs):
    if instance.end_job:
        instance.hours = get_job_hours(instance.start_job, instance.end_job)
        instance.extra_hours = get_extra_job_hours(instance.start_job, instance.end_job)
