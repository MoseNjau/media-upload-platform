from django.urls import path
from .views import MySignupView, MyLoginView, MyLogoutView

app_name = 'authentication'  # Optional, but good practice to namespace your URLs

urlpatterns = [
    path('signup/', MySignupView.as_view(), name='signup'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
]
