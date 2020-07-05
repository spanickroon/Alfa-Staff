"""This module contain functions for activate user."""

from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password, make_password
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from .tokens import account_activation_token


def activate_processing(request: object, uidb64: str, token: str) -> bool:
    """Check user in database after decoding params and changes is_active status and login user."""
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        login(request, user)
        return True
    return False
