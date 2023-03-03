from apps.users.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.users.models import Financials, Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=Profile)
def create_profile_financials(sender, instance, created, **kwargs):
    if created:
        Financials.objects.create(profile=instance)


@receiver(post_save, sender=Profile)
def save_profile_financials(sender, instance, **kwargs):
    instance.financials.save()
