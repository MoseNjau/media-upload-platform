from django.db import models
from django.conf import settings
from django.utils.timezone import now
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User

EXTENSIONS = ['mp4', 'avi', 'wav', 'mov', 'webm']


class Tag(models.Model):
    name = models.CharField(max_length=255)


class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1024)
    file = models.FileField(validators=[FileExtensionValidator(allowed_extensions=EXTENSIONS)])
    upload_date = models.DateTimeField(default=now)
    numberOfViews = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        ordering = ['upload_date']


class Comment(models.Model):
    text = models.CharField(max_length=255)
    post_date = models.DateTimeField(default=now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

    class Meta:
        ordering = ['post_date']


class VideoTag(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)