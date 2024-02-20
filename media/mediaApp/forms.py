from django import forms

class MediaUploadForm(forms.Form):
    title = forms.CharField(max_length=255, label='Title')
    description = forms.CharField(max_length=1024)
    video = forms.FileField(label='Select a video to upload')
    tag = forms.CharField(max_length=255, label='Point tags')


class SearchMediaForm(forms.Form):
    query = forms.CharField(label='Search')

class CommentForm(forms.Form):
    comment_text = forms.CharField(max_length=255, label='Comment')
