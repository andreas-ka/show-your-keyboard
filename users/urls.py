from django.urls import path
from .views import UserRegister, ProfileEdit
from . import views


urlpatterns = [
    path('register/', UserRegister.as_view(), name='register'),
    path('profile_edit/', ProfileEdit.as_view(), name='profile_edit'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
