from django.urls import path
from .views import UserRegister, ProfileEdit

urlpatterns = [
    path('register/', UserRegister.as_view(), name='register'),
    path('profile_edit/', ProfileEdit.as_view(), name='profile_edit'),
]