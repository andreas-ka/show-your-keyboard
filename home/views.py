from django.shortcuts import render
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import CreatePostForm, EditPostForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


"""View for the index or home page"""
class Index(ListView):
    template_name = 'home/index.html'
    model = Post
    context_object_name = 'post'

    def get_queryset(self):
        return self.model.objects.all()[:3]


"""View for seeing all the posts"""
class PostView(ListView):
    model = Post
    template_name = 'home/post_view.html'
    ordering = ['-created']


"""View too see details about a specific post"""
class PostDetailView(DetailView):
    model = Post
    template_name = 'home/post_detail.html'


"""View to create a new post"""
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'home/post_create.html'
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreateView, self).form_valid(form)


"""View to update your post when logged in"""
class PostUpdateView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'home/post_edit.html'
    success_url = reverse_lazy('posts')


"""View to delete your posts"""
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'home/post_delete.html'
    success_url = reverse_lazy('posts')
