"""This module contain functions for signup."""

from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from ..models import Profile
from .email_sender import send_message_with_url_for_registration


def signup_processing(request: object, signup_form: object) -> object:
    """Check user in database and create him after returned user."""
    try:
        user = User.objects.get(email=signup_form.cleaned_data["email"])
        return JsonResponse({"confirmation": "user_found"})
    except Exception:
        pass

    user = User(
        username=signup_form.cleaned_data['email'],
        email=signup_form.cleaned_data['email'],
        password=make_password(signup_form.cleaned_data['password1'])
    )
    user.is_active = True
    user.save()

    profile = Profile(
        user=user
    )
    profile.save()

    return send_message_with_url_for_registration(request, user)
