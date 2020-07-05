"""This module contain functions for calculate page."""

import math

from ..models import Purchase, BonusCard


def count_page_bonuses() -> list:
    """Calculate count page for bonuses."""
    return list(range(1, math.ceil(len(BonusCard.objects.all()) / 8) + 1))


def count_page_purchases(request: object) -> list:
    """Calculate count page for purchases."""
    return list(range(1, math.ceil(len(Purchase.objects.filter(user=request.user)) / 10) + 1))
