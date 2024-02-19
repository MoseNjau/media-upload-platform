# core/urls.py
from django.urls import path
from .views import home_view, post_list_view, post_detail_view, create_post_view, create_comment_view, contact_view

app_name = 'core'

urlpatterns = [
    path('', home_view, name='home'),
    path('post_list/', post_list_view, name='post_list'),
    path('post_detail/<int:post_id>/', post_detail_view, name='post_detail'),
    path('create_post/', create_post_view, name='create_post'),
    path('create_comment/<int:post_id>/', create_comment_view, name='create_comment'),
    path('contact/', contact_view, name='contact'),
]
