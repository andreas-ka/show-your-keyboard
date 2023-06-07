from django.shortcuts import render
from django.views.generic import ListView, DeleteView, DetailView
from .models import Post


class Index(ListView):
    template_name = 'home/index.html'
    model = Post
    context_object_name = 'post'

    def get_queryset(self):
        return self.model.objects.all()[:3]


class PostView(ListView):
    model = Post
    template_name = 'home/post_view.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'home/post_detail.html'