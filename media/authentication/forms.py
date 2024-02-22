from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError, ObjectDoesNotExist
import re
from .models import UserProfile

VALIDATE_EMAIL = re.compile(r"[\w\d]+\.?@[\w\.]+")


class LoginForm(forms.Form):
    username=forms.CharField(max_length=250)
    password=forms.CharField(max_length=12, widget=forms.PasswordInput)

class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
    password = forms.CharField(max_length=12, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=12, widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    date_of_birth = forms.DateField()
    gender = forms.CharField(max_length=10)
    phone_number = forms.CharField(max_length=15)

    def clean_username(self):
        cd = self.cleaned_data
        username = cd.get("username")
        try:
            if User.objects.get(username=username):
                raise ValidationError("Username Exists!!")
        except ObjectDoesNotExist:
            pass
        return username

    def clean_confirm_password(self):
        cd = self.cleaned_data
        _password = cd.get('password')
        _confirm_password = cd.get("confirm_password")
        if _password != _confirm_password:
            raise ValidationError("Passwords do not match!")

    def clean_password(self):
        cd = self.cleaned_data
        password = cd.get("password")
        self.valid_password(password)
        return password

    def clean_email(self):
        cd = self.cleaned_data
        email = cd.get("email")
        match = VALIDATE_EMAIL.match(email)
        if not match:
            raise ValidationError("Invalid email format")
        return email

    def save(self, commit=True):
        cd = self.cleaned_data
        user = User.objects.create_user(
            username=cd['username'],
            email=cd['email'],
            password=cd['password'],
            first_name=cd['first_name'],
            last_name=cd['last_name']
        )
        user.save()
        # Create UserProfile
        UserProfile.objects.create(user=user, date_of_birth=cd['date_of_birth'],
                                   gender=cd['gender'], phone_number=cd['phone_number'])
        return user

    def valid_password(self, password):
        if len(password)< 8:
            raise ValidationError("pasword must be 8 characters or more")
        # test special character
        if not len(re.findall("[!@#\$%\^&*]+", password)):
            raise ValidationError("Password must contain a special character")
            # test upper case
        if not len(re.findall("[A-Z]+",password)):
            raise ValidationError("Password must contain capital letter")
            # validate small letter
        if not len(re.findall("[a-z]+", password)):
            raise ValidationError("Password must contain small letter")
            # validate numbers
        if not len(re.findall("[0-9]+",password)):
            raise ValidationError("Password must contain a digit")
        return True