from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms import RegisterForm, ProfileEditForm
from django.urls import reverse_lazy, reverse
from .models import Profile
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def login_user(request):
    """Login form and messages"""
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been successfully logged in.")
            return redirect("home")
        else:
            messages.error(request, "There was an error during login.")
            return redirect("login")
    else:
        return render(
            request, "register/login.html",
            {"messages": messages.get_messages(request)}
        )


class UserRegister(generic.CreateView):
    """View for user registration"""

    form_class = RegisterForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")


class ProfileEdit(generic.UpdateView):
    """View for edit your profile"""

    model = Profile
    form_class = ProfileEditForm
    template_name = "registration/profile.html"
    success_url = reverse_lazy("posts")

    def get_object(self):
        return self.request.user.profile
