"""This module contain classes for work with forms."""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    """SignupForm class with meta data for signup."""

    class Meta:
        """Meta data."""

        model = User
        fields = ('email', 'password1', 'password2')


class LoginForm(forms.ModelForm):
    """LoginForm class with meta data for login."""

    class Meta:
        """Meta data."""

        model = User
        fields = ('email', 'password')


class ResetPasswordForm(forms.ModelForm):
    """ResetPasswordForm class with meta data for reset password."""

    class Meta:
        """Meta data."""

        model = User
        fields = ('email', )
