from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import LoginForm, UserRegistrationForm
from .models import UserProfile
from django.contrib.auth.mixins import LoginRequiredMixin

class MyLoginView(CreateView):
    template_name = 'authentication/login.html'
    form_class = LoginForm

    def form_valid(self, form):
        cd = form.cleaned_data
        username = cd["username"]
        password = cd["password"]
        user = authenticate(self.request, username=username, password=password)
        if user:
            login(self.request, user)
            return HttpResponse("success")
        else:
            return HttpResponse("Failed")

    def get(self, request, *args, **kwargs):
        self.object = None
        return super().render_to_response(self.get_context_data())

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.pop('instance', None)  # Remove 'instance' from the kwargs
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context

class MySignupView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'authentication/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Account created successfully. Please log in.')

        # Log in the user after successful registration
        user = authenticate(
            self.request,
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)

        return response

    def get(self, request, *args, **kwargs):
        self.object = None
        return super().render_to_response(self.get_context_data())

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.pop('instance', None)  # Remove 'instance' from the kwargs
        return kwargs
    
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserRegistrationForm
    template_name = 'profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user.userprofile

    def form_valid(self, form):
        user_profile = form.save(commit=False)
        user_profile.date_of_birth = form.cleaned_data['date_of_birth']
        user_profile.gender = form.cleaned_data['gender']
        user_profile.phone_number = form.cleaned_data['phone_number']
        user_profile.save()
        messages.success(self.request, 'Profile updated successfully.')
        return super().form_valid(form)

class LogoutView(LoginRequiredMixin, CreateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('home')  # Replace 'home' with your desired redirect URL
