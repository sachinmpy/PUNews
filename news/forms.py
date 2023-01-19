from django.forms import ModelForm
from django import forms
from .models import News


#HANDLE THIS
class NewsCreationForm(ModelForm):
    posted_by = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'True'}))
    class Meta:
        model = News
        fields = '__all__'