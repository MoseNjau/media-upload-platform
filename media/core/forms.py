from django import forms
from .models import Contact

class UploadPhotoForm(forms.Form):
    image = forms.ImageField(label='Select a profile picture')

class EditVideoInfoForm(forms.Form):
    title = forms.CharField(max_length=255)
    description = forms.CharField(widget=forms.Textarea)

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
        }
