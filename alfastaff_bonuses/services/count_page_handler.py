"""This module contain functions for calculate page."""

import math

from ..models import Purchase, BonusCard


def count_page_bonuses() -> str:
    """Calculate count page for bonuses."""
    return "".join(map(str, list(range(1, math.ceil(len(BonusCard.objects.all()) / 8) + 1))))


def count_page_purchases() -> str:
    """Calculate count page for purchases."""
    return "".join(map(str, list(range(1, math.ceil(len(Purchase.objects.all()) / 10) + 1))))
