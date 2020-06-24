from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email', 'password')


class ResetPasswordForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('email', )
