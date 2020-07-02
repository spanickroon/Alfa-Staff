"""This module contain functions for bonuses page."""

from django.core.paginator import Paginator

from ..models import BonusCard


def get_bonuses(request: object, page_num: int, sort: str) -> list:
    """Calculate bonuses object for page."""
    if sort == "sort_cost":
        bonuses = BonusCard.objects.order_by("-cost")
    else:
        bonuses = BonusCard.objects.all()

    paginator = Paginator(bonuses, 8)

    return paginator.page(page_num)
