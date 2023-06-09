from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
from .models import Post
from django.http import HttpResponseRedirect
from .forms import CreatePostForm, EditPostForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum, Count


"""View for the index or home page"""
class Index(ListView):
    template_name = 'home/index.html'
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['total_likes'] = Post.objects.all().aggregate(sum_all=Sum('likes')).get('sum_all')
        post_numbers = Post.objects.all().count()
        context['post_numbers'] = post_numbers
        return context


"""View for seeing all the posts"""
class PostView(ListView):
    model = Post
    template_name = 'home/post_view.html'
    ordering = ['-created']


"""View too see details about a specific post"""
class PostDetailView(DetailView):
    model = Post
    template_name = 'home/post_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs) 

        get_post = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = get_post.total_likes()

        liked = False
        if get_post.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


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


"""View to see likes"""
def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_like_btn'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))
