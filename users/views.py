from django.shortcuts import render
from django.views.generic import UpdateView
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms import RegisterForm, ProfileEditForm
from django.urls import reverse_lazy, reverse
from .models import Profile
from django.contrib import messages


class UserRegister(generic.CreateView):
    """ View for user registration """
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class ProfileEdit(generic.UpdateView):
    """ View for edit your profile """
    model = Profile
    form_class = ProfileEditForm
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('posts')

    def get_object(self):
        return self.request.user.profile