from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username','email', 'password1', 'password2']

    first_name = forms.CharField(required=True,max_length=15,)
    last_name = forms.CharField(required=True,max_length=15)
    email = forms.EmailField(required=True,help_text='abc@xyz.com')




