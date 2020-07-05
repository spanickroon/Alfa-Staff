"""This module contain functions for buy product on catalog."""

from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import redirect

from ..models import Purchase, BonusCard
from .email_sender import send_message_about_buy


def buy_processing(request: object, id: int) -> object:
    """Buy ptodunct and send message on email admin."""
    try:
        user = User.objects.get(email=request.user.email)
        bonus = BonusCard.objects.get(id=id)

        if user.profile.points - bonus.cost < 0:
            return JsonResponse({"buy": "not_points"})

        user.profile.points = user.profile.points - bonus.cost
        user.profile.save()

        purchase = Purchase(
            user=user,
            name=bonus.name,
            id_purchase=len(Purchase.objects.filter(user=request.user)) + 1,
            cost=bonus.cost,
            balance=user.profile.points,
            status=3
        )
        purchase.save()

        return send_message_about_buy(request, user, bonus)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        return JsonResponse({"buy": "error"})
