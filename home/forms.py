from django import forms
from .models import Post, Comment


class CreatePostForm(forms.ModelForm):
    """ Create a new post form """
    class Meta:
        model = Post
        fields = ('title', 'description', 'case', 'switches', 'keycaps',
                  'tags', 'image')

        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'case': forms.TextInput(attrs={'class': 'form-control'}),
            'switches': forms.TextInput(attrs={'class': 'form-control'}),
            'keycaps': forms.TextInput(attrs={'class': 'form-control'}),
            'tags': forms.TextInput(attrs={'class': 'form-control'}),
        }


class EditPostForm(forms.ModelForm):
    """ Edit post form """
    class Meta:
        model = Post
        fields = ('title', 'description', 'case', 'switches',
                  'keycaps', 'tags')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'case': forms.TextInput(attrs={'class': 'form-control'}),
            'switches': forms.TextInput(attrs={'class': 'form-control'}),
            'keycaps': forms.TextInput(attrs={'class': 'form-control'}),
            'tags': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CommentPostForm(forms.ModelForm):
    """ Comment form """
    class Meta:
        model = Comment
        fields = ('body',)

        widgets = {
            'body': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }
