from django.db.models.signals import post_save
from django.dispatch import receiver
from account.models import User
from drive.models import DriveFolder

@receiver(post_save, sender=User)
# user post create signal -> create a folder with the user's name
def create_user_folder(sender, instance, created, **kwargs):
    if created:
        DriveFolder.objects.create(user=instance, path="/")
