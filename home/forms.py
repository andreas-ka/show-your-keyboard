from django import forms
from .models import Post


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'description', 'case', 'switches', 'keycaps', 'tags')

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
    class Meta:
        model = Post
        fields = ('title', 'description', 'case', 'switches', 'keycaps', 'tags')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'case': forms.TextInput(attrs={'class': 'form-control'}),
            'switches': forms.TextInput(attrs={'class': 'form-control'}),
            'keycaps': forms.TextInput(attrs={'class': 'form-control'}),
            'tags': forms.TextInput(attrs={'class': 'form-control'}),
        }
