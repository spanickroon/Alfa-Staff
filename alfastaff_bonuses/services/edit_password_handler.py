"""This module contain functions for edit password."""

from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password, make_password

from .dropbox_handler import get_avatars_from_dropbox


def edit_password_processing(request: object, password_change_form: object) -> object:
    """Change user password."""
    user = User.objects.get(email=request.user.email)

    avatar = get_avatars_from_dropbox(user)

    password1 = password_change_form.cleaned_data.get("password1")
    password2 = password_change_form.cleaned_data.get("password2")

    if password1 and password2 and password1 != password2:
        return render(
            request, template_name='alfastaff-bonuses/edit.html',
            context={'user': request.user, 'error': True, 'avatar': avatar})

    user.password = make_password(password2)
    user.save()

    login(request, user)
    return redirect(to="edit")
