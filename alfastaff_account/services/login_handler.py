"""This module contain functions for login."""

from django.http import JsonResponse
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password


def login_processing(request: object, login_form: object) -> None:
    """Check user in database and login him if user exist."""
    try:
        user = User.objects.get(email=login_form.cleaned_data["email"])

        if not check_password(login_form.cleaned_data["password"], user.password):
            return JsonResponse({"validation": "password_incorrect"})

        login(request, user)
        return JsonResponse({"validation": "ok"})
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        return JsonResponse({"validation": "user_not_found"})
