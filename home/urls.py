from django.urls import path
from .views import Index, PostView, PostDetailView, PostCreateView, PostUpdateView

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('posts', PostView.as_view(), name="posts"),
    path('posts/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('create', PostCreateView.as_view(), name='post_create'),
    path('edit/<int:pk>', PostUpdateView.as_view(), name='post_edit'),

]
