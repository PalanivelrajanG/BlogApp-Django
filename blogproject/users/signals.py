from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# Signal handler to create a profile for a new user
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:  # Check if the user instance is newly created
        Profile.objects.create(user=instance)

# Signal handler to save the profile when the user is saved
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    try:
        instance.profile.save()  # Attempt to save the profile
    except Profile.DoesNotExist:
        Profile.objects.create(user=instance)  # If profile does not exist, create it
