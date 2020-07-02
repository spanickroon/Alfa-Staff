"""This module contain functions for bonuses page."""

from ..models import BonusCard


def get_bonuses(request: object, page: int, sort: str) -> list:
    """Calculate bonuses object for page."""
    if sort == "sort_cost":
        bonuses = BonusCard.objects.order_by("-cost")
    else:
        bonuses = BonusCard.objects.all()

    if (page * 8) - 8 >= len(bonuses):
        bonuses = bonuses[(len(bonuses) // 8) * 8:len(bonuses)]
    else:
        if len(bonuses) > 8 and len(bonuses) % 8 == 0:
            bonuses = bonuses[(8 * page) - 8:(8 * page)]
        elif len(bonuses) > 8 and len(bonuses) % 8 != 0:
            if (8 * page) < len(bonuses):
                bonuses = bonuses[(8 * page) - 8:(8 * page)]
            else:
                bonuses = bonuses[(8 * page) - 8:len(bonuses)]

    return bonuses
