"""This module contain functions for calculate page."""

import math

from ..models import Purchase, ProductCard


def count_page_products() -> list:
    """Calculate count page for products."""
    return list(range(1, math.ceil(len(ProductCard.objects.all()) / 8) + 1))


def count_page_purchases(request: object) -> list:
    """Calculate count page for purchases."""
    return list(range(1, math.ceil(len(Purchase.objects.filter(user=request.user)) / 10) + 1))
