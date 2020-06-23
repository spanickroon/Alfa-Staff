from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from alfastaff_account.models import Profile


class PasswordChangeForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('password1', 'password2')


class ProfileChangeForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ('avatar', 'first_name', 'second_name', 'middle_name', 'number_phone', 'position', 'department',)
