from django.contrib import admin
from .models import Video, VideoTag, Comment

# Register your models here.
admin.site.register(Video)
admin.site.register(VideoTag)
admin.site.register(Comment)