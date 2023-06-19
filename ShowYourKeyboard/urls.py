from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
]

""" Error handlers """

HANDLER404 = "ShowYourKeyboard.views.page_not_found_view"
HANDLER500 = "ShowYourKeyboard.views.custom_500_error_view"
HANDLER403 = "ShowYourKeyboard.views.custom_403_error_view"
