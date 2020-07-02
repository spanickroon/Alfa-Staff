"""This module contain functions for reset password."""

from django.http import JsonResponse
from django.contrib.auth.models import User

from .email_sender import send_message_with_new_password


def reset_password_processing(request: object, reset_password_form: object) -> object:
    """Check user in database and send email."""
    try:
        user = User.objects.get(email=reset_password_form.cleaned_data["email"])
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        return JsonResponse({"reseting": "user_not_found"})

    return send_message_with_new_password(request, user)
