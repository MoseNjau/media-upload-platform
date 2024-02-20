from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings
from django.contrib.auth.models import User

# Define GENDER_CHOICES here
GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other')
]

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='O')
    phone_number = PhoneNumberField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfiles'

    def __str__(self) -> str:
        return self.user.username