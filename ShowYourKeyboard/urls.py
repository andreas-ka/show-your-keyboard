from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
]

handler404 = 'home.views.error_404'
