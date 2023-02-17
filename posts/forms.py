from django.forms import ModelForm, TextInput
from django import forms
from .models import Post
from user_models.models import User

class PostCreationForm(ModelForm):

    class Meta:
        model = Post
        fields = ('posted_by', 'content')
