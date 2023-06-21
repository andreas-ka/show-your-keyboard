from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
    ListView,
    DeleteView,
    DetailView,
    CreateView,
    UpdateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib import messages
from django.contrib.messages import get_messages
from .models import Post, Comment
from .forms import CreatePostForm, EditPostForm, CommentPostForm


class Index(ListView):
    """View for the index or home page"""

    template_name = "home/index.html"
    model = Post
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        """ Get total posts, total likes, and latest post and comments """
        context = super().get_context_data(**kwargs)
        post_numbers = Post.objects.all().count()
        context["post_numbers"] = post_numbers

        latest_comments = Comment.objects.order_by("-created_on")[:3]
        context["latest_comments"] = latest_comments

        latest_posts = Post.objects.order_by("-created")[:3]
        context["latest_posts"] = latest_posts

        context["messages"] = messages.get_messages(self.request)

        total_likes = 0
        for post in context["post"]:
            total_likes += post.likes.count()
            context["total_likes"] = total_likes

        return context


class PostView(ListView):
    """View for seeing all the posts"""

    model = Post
    template_name = "home/post_view.html"
    ordering = ["-created"]


class PostDetailView(DetailView):
    """View too see details about a specific post"""

    model = Post
    form_class = CommentPostForm
    template_name = "home/post_detail.html"

    """ Get total likes for the specific post and display it
    Set the comment form """
    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentPostForm()

        get_post = get_object_or_404(Post, id=self.kwargs["pk"])
        total_likes = get_post.total_likes()

        liked = False
        if get_post.likes.filter(id=self.request.user.id).exists():
            liked = True

        profile = None
        if self.request.user.is_authenticated:
            profile = self.request.user.profile

        context["profile"] = profile
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

    def post(self, request, *args, **kwargs):
        """ Creates the comments and displays all comments """

        queryset = Post.objects.all
        post = get_object_or_404(Post, id=self.kwargs["pk"])
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
            {"post": post, "comment_form": comment_form, "liked": liked},
        )


class PostCreateView(LoginRequiredMixin, CreateView):
    """View to create a new post"""

    model = Post
    form_class = CreatePostForm
    template_name = "home/post_create.html"
    success_url = reverse_lazy("posts")

    def form_valid(self, form):
        """ Check so the form is valid """
        form.instance.user = self.request.user
        return super(PostCreateView, self).form_valid(form)


class PostUpdateView(UpdateView):
    """View to update your post when logged in"""

    model = Post
    form_class = EditPostForm
    template_name = "home/post_edit.html"
    success_url = reverse_lazy("posts")


class PostDeleteView(DeleteView):
    """View to delete your posts"""

    model = Post
    template_name = "home/post_delete.html"
    success_url = reverse_lazy("posts")

    def get_object(self, queryset=None):
        return get_object_or_404(Post, pk=self.kwargs.get('pk'))


def LikeView(request, pk):
    """View to see likes"""
    post = get_object_or_404(Post, id=request.POST.get("post_like_btn"))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse("post_detail", args=[str(pk)]))


class SearchResultsView(ListView):
    """Search the website and posts"""

    model = Post
    template_name = "home/search_results.html"

    def get_queryset(self):
        """ Query the object_list to get all posts that matches the search """
        query = self.request.GET.get("q")
        object_list = Post.objects.filter(
            Q(title__icontains=query)
            | Q(description__icontains=query)
            | Q(tags__icontains=query)
            | Q(user__username__icontains=query)
            | Q(keycaps__icontains=query)
            | Q(case__icontains=query)
            | Q(switches__icontains=query)
        )
        return object_list


def custom_page_not_found_view(request, exception):
    """ Render error template """
    return render(request, "templates/404.html", {})


def custom_error_view(request, exception=None):
    """ Render error template """
    return render(request, "templates/500.html", {})


def custom_permission_denied_view(request, exception=None):
    """ Render error template """
    return render(request, "templates/403.html", {})
