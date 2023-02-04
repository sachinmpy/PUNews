from django.forms import ModelForm, TextInput
from django import forms
from .models import News
from user_models.models import User


#HANDLE THIS
class NewsCreationForm(ModelForm):
    # posted_by = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'True'}))
    class Meta:
        model = News
        exclude = ('approved_by', 'is_approved')