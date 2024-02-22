from django.shortcuts import render 
from django.views.generic.list import ListView
from mediaApp.models import Video
from django.contrib.auth.models import User
from django.views import View
from django.db.models import Q
from media import settings
from django.shortcuts import HttpResponse, redirect
from .forms import UploadPhotoForm, EditVideoInfoForm

from django.views.generic.edit import FormView
from .forms import ContactForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import Contact


class ProfileView(ListView):
    template_name = 'core/profile.html'
    paginate_by = 3
    context_object_name = 'data'
    model = Video

    def get_queryset(self):
        user_id = self.kwargs['userid']
        user = User.objects.get(pk=user_id)
        videos = Video.objects.filter(Q(author=user))
        return videos

    def get_context_data(self, *, object_list=None, **kwargs):
        user_id = self.kwargs['userid']
        context = super(ProfileView, self).get_context_data(**kwargs)
        user = User.objects.get(id=user_id)
        context['photoform'] = UploadPhotoForm
        context['editform'] = EditVideoInfoForm
        context['name'] = user.username
        context['profile'] = user.profile
        return context

    def post(self, request, userid, *args):
        image = request.FILES['image']
        user = User.objects.get(pk=userid)
        user.profile.pfp = image
        user.save()
        return redirect(f'/core/profile/{userid}')


class PfpView(View):

    def get(self, request, pfpname):
        with open(settings.MEDIA_ROOT + 'pfile/' + pfpname, 'rb') as pfp:
            return HttpResponse(content=pfp, content_type='image/jpeg*')


class ContactView(FormView):
    template_name = 'contact/contact_form.html'  # Create an HTML template for your contact form
    form_class = ContactForm

    def form_valid(self, form):
        # If the form is valid, save the contact information to the database
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']

        # Save the contact information to the database
        Contact.objects.create(name=name, email=email, message=message, timestamp=timezone.now())

        # Redirect to a success page (you can customize this URL)
        return HttpResponseRedirect(reverse('contact:success'))

    def form_invalid(self, form):
        # If the form is invalid, render the form again with error messages
        return self.render_to_response(self.get_context_data(form=form))

# Create a success view (you can customize the HTML template)
class ContactSuccessView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contact/success.html')  # Create an HTML template for your success page
