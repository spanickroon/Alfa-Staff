"""This module contain functions for buy product on catalog."""

from django.http import JsonResponse
from django.contrib.auth.models import User

from ..models import Purchase, ProductCard
from .email_sender import send_message_about_buy


def buy_processing(request: object, id: int) -> object:
    """Buy ptodunct and send message on email admin."""
    try:
        user = User.objects.get(email=request.user.email)
        product = ProductCard.objects.get(id=id)

        if user.profile.money - product.cost < 0:
            return JsonResponse({"buy": "not_money"})

        user.profile.money = user.profile.money - product.cost
        user.profile.save()

        purchase = Purchase(
            user=user,
            name=product.name,
            id_purchase=len(Purchase.objects.filter(user=request.user)) + 1,
            cost=product.cost,
            balance=user.profile.money,
            status=3
        )
        purchase.save()

        return send_message_about_buy(request, user, product)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        return JsonResponse({"buy": "error"})
