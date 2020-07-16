"""This module contain functions for edit profile."""

from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import redirect


def edit_profile_processing(request: object, profile_change_form: object) -> object:
    """Change user data in profile."""
    user = User.objects.get(email=request.user.email)
    user.email = profile_change_form.cleaned_data.get('email')

    if profile_change_form.cleaned_data.get('avatar') != "images/profiles/anon_user.png":
        user.profile.avatar = profile_change_form.cleaned_data.get('avatar')

    user.profile.first_name = profile_change_form.cleaned_data.get('first_name')
    user.profile.second_name = profile_change_form.cleaned_data.get('second_name')
    user.profile.middle_name = profile_change_form.cleaned_data.get('middle_name')
    user.profile.number_phone = profile_change_form.cleaned_data.get('number_phone')

    user.profile.save()
    user.save()

    login(request, user)
    return redirect(to="edit")
