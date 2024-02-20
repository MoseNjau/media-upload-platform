from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserProfileForm
from django.contrib import messages

class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'authentication/register.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        user_profile_form = UserProfileForm(self.request.POST, instance=self.object)

        if user_profile_form.is_valid():
            user_profile_form.save()
            messages.success(self.request, 'Account created successfully. Please log in.')

        return response


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'authentication/login.html'


class MyLogoutView(LogoutView):
    # You can add any additional logic after logout if needed
    next_page = reverse_lazy('home')  # Replace 'home' with your desired redirect URL
