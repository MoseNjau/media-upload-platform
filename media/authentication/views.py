# authentication/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserProfileForm, UserRegistrationForm
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Add any additional logic after login if needed
                return redirect('home')  # Replace 'home' with your desired redirect URL
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'authentication/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            # Add any additional logic after registration if needed
            messages.success(request, 'Account created successfully. Please log in.')
            return redirect('login')  # Replace 'login' with your login URL
    else:
        user_form = UserRegistrationForm()
        profile_form = UserProfileForm()

    return render(request, 'authentication/register.html', {'user_form': user_form, 'profile_form': profile_form})

def logout_view(request):
    logout(request)
    # Add any additional logic after logout if needed
    return redirect('home')  # Replace 'home' with your desired redirect URL

# Additional view for account verification (assuming email verification)
# This could involve sending a verification email to the user's email address
# and updating the UserProfile to mark the account as verified upon confirmation.
# The implementation would depend on your chosen method for email verification.
