from django.forms import ModelForm
from user_models.models import User

class UserRegisterForm(ModelForm):
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name', 'designation', 'department')
        # fields = '__all__'

class UserLoginForm(ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')