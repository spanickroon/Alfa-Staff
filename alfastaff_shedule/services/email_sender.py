"""This module contain functions for send email message."""

from django.http import JsonResponse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import format_html
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
from datetime import datetime
from pathlib import Path
import requests


def send_message_with_review(request: object, user: object, review: str) -> object:
    """Send message with review on email admin."""
    current_site = get_current_site(request)
    mail_subject = 'Отзыв о расписании'

    message = render_to_string('alfastaff-shedule/review_message.html', {
        'user': user,
        'review': review,
        'domain': current_site.domain,
        'time': datetime.now().strftime('%d.%m.%Y в %H:%M:%S')
    })

    to_email = settings.EMAIL_HOST_USER

    email = EmailMultiAlternatives(mail_subject, message, to=[to_email])

    email.content_subtype = 'html'
    email.attach_alternative(message, "text/html")
    email.mixed_subtype = 'related'

    email.send()
    return JsonResponse({"send": "ok"})