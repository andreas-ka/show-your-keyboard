from django.shortcuts import render
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import CreatePostForm, EditPostForm


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


class PostCreateView(CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'home/post_create.html'


class PostUpdateView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'home/post_edit.html'
    #fields = ['title', 'description', 'case', 'switches', 'keycaps', 'tags']