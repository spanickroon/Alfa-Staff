"""This module contain functions for purchases page."""

from ..models import Purchase


def get_purchases(request: object, page: int, sort: str) -> list:
    """Calculate purchases object for page."""
    if sort == "sort_cost":
        purchases = Purchase.objects.filter(user=request.user).order_by("-cost")
    else:
        purchases = Purchase.objects.filter(user=request.user)

    if (page * 10) - 10 >= len(purchases):
        purchases = purchases[(len(purchases) // 10) * 10:len(purchases)]
    else:
        if len(purchases) > 10 and len(purchases) % 8 == 0:
            purchases = purchases[(10 * page) - 10:(10 * page)]
        elif len(purchases) > 10 and len(purchases) % 10 != 0:
            if (10 * page) < len(purchases):
                purchases = purchases[(10 * page) - 10:(10 * page)]
            else:
                purchases = purchases[(10 * page) - 10:len(purchases)]

    return purchases
