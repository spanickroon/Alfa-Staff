"""This module contain functions for send review on admin email."""

from django.http import JsonResponse

from .email_sender import send_message_with_review


def send_review_processing(request: object) -> object:
    """Send message on email admin."""
    try:
        review = request.POST.get('review_text')

        return send_message_with_review(request, request.user, review)
    except (TypeError, ValueError, OverflowError):
        return JsonResponse({"send": "error"})