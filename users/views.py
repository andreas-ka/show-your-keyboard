from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import RegisterForm, ProfileEditForm
from .models import Profile


def login_user(request):
    """Login form and messages"""
    if request.method == "POST":
        username = request.POST["username"]
        print('USERNAME: ', username)
        password = request.POST["password"]
        print('PASSWORD: ', password)
        user = authenticate(request, username=username, password=password)
        print('REQUEST = POST')
        if user is not None:
            login(request, user)
            messages.success(request, "You have been successfully logged in.")
            return redirect("home")
        else:
            messages.error(request, "There was an error during login.")
            return redirect("login")
    else:
        return render(request, "registration/login.html")


def logout_user(request):
    """ Logout user """
    logout(request)
    messages.error(request, "You have been successfully logged out.")
    return redirect("home")


class UserRegister(generic.CreateView):
    """View for user registration"""

    form_class = RegisterForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")


class ProfileEdit(LoginRequiredMixin, generic.UpdateView):
    """View for edit your profile"""

    model = Profile
    form_class = ProfileEditForm
    template_name = "registration/profile.html"
    success_url = reverse_lazy("posts")

    def get_object(self):
        """ Define the get object to user profile """
        return self.request.user.profile
