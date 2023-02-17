from apps.users.models import Financials, Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_user_profile_and_financials(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        Financials.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile_and_financials(sender, instance, **kwargs):
    instance.profile.save()
    instance.financials.save()
