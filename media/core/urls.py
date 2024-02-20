from django.urls import path
from .views import ProfileView, PfpView, ContactView, ContactSuccessView

app_name = 'core'

urlpatterns = [
    path('profile/<int:userid>/', ProfileView.as_view(), name='profile'),
    path('pfp/<str:pfpname>/', PfpView.as_view(), name='pfp'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('contact/success/', ContactSuccessView.as_view(), name='success'),
]
