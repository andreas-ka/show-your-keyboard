from django.shortcuts import render
from django.views.generic import UpdateView
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms import RegisterForm, ProfileEditForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin

""" View for user registration """
class UserRegister(generic.CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


""" View for edit your profile """
class ProfileEdit(generic.UpdateView):
    form_class = ProfileEditForm
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('posts')

    def get_object(self):
        return self.request.user