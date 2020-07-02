"""This module contain functions for send email message."""

from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings


def send_message_about_buy(request: object, user: object) -> None:
    """Send message about buy product on email admin."""
    current_site = get_current_site(request)
    mail_subject = 'Buy bonuses.'
    message = render_to_string('alfastaff-bonuses/buy_message.html', {
        'user': user,
        'domain': current_site.domain,
    })
    to_email = settings.EMAIL_HOST_USER
    email = EmailMessage(mail_subject, message, to=[to_email])

    email.send()
    return JsonResponse({"buy": "ok"})
