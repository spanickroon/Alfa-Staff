"""This module contain functions for bonuses page."""

from django.core.paginator import Paginator

from ..models import ProductCard


def get_products(request: object, page_num: int, sort: str) -> list:
    """Calculate products object for page."""
    if sort == "sort_cost":
        products = ProductCard.objects.order_by("-cost")
    else:
        products = ProductCard.objects.all()

    paginator = Paginator(products, 8)

    return paginator.page(page_num)
