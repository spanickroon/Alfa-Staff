"""This module contain classes for work with forms."""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from alfastaff_account.models import Profile


class PasswordChangeForm(UserCreationForm):
    """PasswordChangeForm class with meta data for password change."""

    class Meta:
        """Meta data."""

        model = User
        fields = ('password1', 'password2')


class ProfileChangeForm(forms.ModelForm):
    """ProfileChangeForm class with meta data for profile change."""

    email = forms.EmailField()

    class Meta:
        """Meta data."""

        model = Profile
        fields = (
            'avatar', 'email', 'first_name', 'second_name', 'middle_name',
            'number_phone', 'position', 'department',)
