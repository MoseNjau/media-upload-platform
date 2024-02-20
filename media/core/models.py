from django.db import models
from django.contrib.auth.models import User
from mediaApp.models import Video
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.db.models.signals import post_save
from django.dispatch import receiver



class Profile(models.Model):
    user = models.OneToOneField('authentication.UserProfile', on_delete=models.CASCADE, related_name='profile')
    pfp = ProcessedImageField(upload_to='pfps/',
                              processors=[ResizeToFill(100, 100)],
                              format='JPEG',
                              options={'quality': 60},
                              default='pfps/default_pfp.jpeg')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)