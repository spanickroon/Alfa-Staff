"""This module contain functions for purchases page."""

from django.core.paginator import Paginator

from ..models import Purchase


def get_purchases(request: object, page_num: int, sort: str) -> list:
    """Calculate purchases object for page."""
    if sort == "sort_cost":
        purchases = Purchase.objects.filter(user=request.user).order_by("-cost")
    else:
        purchases = Purchase.objects.filter(user=request.user)

    paginator = Paginator(purchases, 10)

    return paginator.page(page_num)
