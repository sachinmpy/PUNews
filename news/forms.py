from django.forms import ModelForm, TextInput
from django import forms
from .models import News
from user_models.models import User


#HANDLE THIS
class NewsCreationForm(ModelForm):
    # posted_by = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'True'}))
    class Meta:
        model = News
        fields = ('posted_by','headline', 'content', 'department', 'link_to_banner')
        widgets = {
            'posted_by': forms.TextInput(attrs={
                'readonly': True,
            })
        }