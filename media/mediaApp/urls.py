from django.urls import path
from .views import Index, Upload, Viewer, FileViewer, ThumbViewer, DeleteVideoView, EditVideoInfoView

app_name = 'mediaApp'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('upload/', Upload.as_view(), name='upload'),
    path('watch/<int:video_id>/', Viewer.as_view(), name='watch'),
    path('file/<str:file_name>/', FileViewer.as_view(), name='file'),
    path('thumb/<str:file_name>/', ThumbViewer.as_view(), name='thumb'),
    path('delete/<int:video_id>/', DeleteVideoView.as_view(), name='delete'),
    path('edit/<int:video_id>/', EditVideoInfoView.as_view(), name='edit'),
]
