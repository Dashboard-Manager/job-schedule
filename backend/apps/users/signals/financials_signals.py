from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.users.models import User, Financials


@receiver(post_save, sender=User)
def create_financials(sender, instance, created, **kwargs):
    if created:
        Financials.objects.create(profile=instance)


@receiver(post_save, sender=User)
def save_financials(sender, instance, **kwargs):
    instance.financials.save()
