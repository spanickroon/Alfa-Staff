"""This module contain functions for send email message."""

from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.conf import settings
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.base_user import BaseUserManager

from .tokens import account_activation_token


def send_message_with_url_for_registration(request: object, user: object) -> None:
    """Send message for registration user on we site."""
    current_site = get_current_site(request)
    mail_subject = 'Activate your account.'
    message = render_to_string('alfastaff-account/email_message.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
    })
    to_email = user.email
    email = EmailMessage(mail_subject, message, to=[to_email])
    email.send()

    return JsonResponse({"confirmation": "ok"})


def send_message_with_new_password(request: object, user: object) -> None:
    """Send message with new password and generated him."""
    new_password = BaseUserManager().make_random_password()

    current_site = get_current_site(request)
    mail_subject = 'Activate your account.'
    message = render_to_string('alfastaff-account/reset_message.html', {
        'user': user,
        'domain': current_site.domain,
        'new_password': new_password
    })
    to_email = user.email

    user.password = make_password(new_password)
    user.save()

    email = EmailMessage(mail_subject, message, to=[to_email])
    email.send()

    return JsonResponse({"reseting": "ok"})
