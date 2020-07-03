"""This module contain functions for send email message."""

from django.http import JsonResponse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import format_html
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
from datetime import datetime
from email.mime.image import MIMEImage
from pathlib import Path


def send_message_about_buy(request: object, user: object, bonus: object) -> None:
    """Send message about buy product on email admin."""
    current_site = get_current_site(request)
    mail_subject = 'Покупка товара'

    bonus_image = Path(f'static/images/{bonus.image}').name

    message = render_to_string('alfastaff-bonuses/buy_message.html', {
        'user': user,
        'domain': current_site.domain,
        'bonus': bonus,
        'bonus_image': bonus_image,
        'time': datetime.now().strftime('%d.%m.%Y в %H:%M:%S')
    })

    to_email = settings.EMAIL_HOST_USER

    email = EmailMultiAlternatives(mail_subject, message, to=[to_email])

    email.content_subtype = 'html'
    email.attach_alternative(message, "text/html")
    email.mixed_subtype = 'related'

    with open(f'static/images/{bonus.image}', mode='rb') as f:
        image = MIMEImage(f.read())
        image.add_header('Content-ID', f"<{bonus_image}>")
        email.attach(image)

    email.send()
    return JsonResponse({"buy": "ok"})
