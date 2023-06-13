from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
from .models import Post, Comment
from django.http import HttpResponseRedirect
from .forms import CreatePostForm, EditPostForm, CommentPostForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum, Count
from django.db.models import Q


"""View for the index or home page"""
class Index(ListView):
    template_name = 'home/index.html'
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_numbers = Post.objects.all().count()
        context['post_numbers'] = post_numbers

        latest_comments = Comment.objects.order_by('-created_on')[:3]
        context['latest_comments'] = latest_comments

        latest_posts = Post.objects.order_by('-created')[:3]
        context['latest_posts'] = latest_posts

        total_likes = 0
        for post in context['post']:
            total_likes += post.likes.count()
        context['total_likes'] = total_likes


        return context


"""View for seeing all the posts"""
class PostView(ListView):
    model = Post
    template_name = 'home/post_view.html'
    ordering = ['-created']


"""View too see details about a specific post"""
class PostDetailView(DetailView):
    model = Post
    form_class = CommentPostForm
    template_name = 'home/post_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context = super().get_context_data(**kwargs) 
        context['comment_form'] = CommentPostForm()

        get_post = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = get_post.total_likes()

        liked = False
        if get_post.likes.filter(id=self.request.user.id).exists():
            liked = True

        profile = self.request.user.profile

        context["profile"] = profile
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

    def post(self, request, *args, **kwargs):

        queryset = Post.objects.all
        post = get_object_or_404(Post, id=self.kwargs['pk'])
        comments = post.comments.order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentPostForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.user_profile = self.request.user.profile.user
            comment.save()
            return redirect(request.path)
        else:
            comment_form = CommentPostForm(request.POST)

        return render(
            request,
            "home/post_detail.html",
            {
                "post": post,
                "comment_form": comment_form,
                "liked": liked
            },
        )


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


""" Search the website and posts """
class SearchResultsView(ListView):
    model = Post
    template_name = 'home/search_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Post.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
        return object_list