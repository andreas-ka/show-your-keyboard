from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import User, Profile
from cloudinary.models import CloudinaryField

### Register on the site form ###
class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput({'class': 'form-control'}))
    first_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = CloudinaryField('image', blank=True, null=True)


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

### Edit your profile form ###
class ProfileEditForm(forms.ModelForm):
    image = CloudinaryField('image', blank=True, null=True)

    class Meta:
        model = Profile
        fields = ('keyboards', 'image',)

        widgets = {
            'keyboards': forms.TextInput(attrs={'class': 'form-control'}),
        }