from django.urls import path
from .views import MySignupView, MyLoginView, LogoutView

app_name = 'authentication'

urlpatterns = [
    path('signup/', MySignupView.as_view(), name='signup'),
    path('login/', MyLoginView.as_view(), name='login'),
    # path('profile/', ProfileUpdateView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
