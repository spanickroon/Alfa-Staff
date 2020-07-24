"""This module contain functions for bonuses page."""

from django.core.paginator import Paginator

from ..models import BonusCard

from base64 import b64encode


def get_bonuses(request: object, page_num: int, sort: str) -> list:
    """Calculate bonuses object for page."""
    if sort == "sort_cost":
        bonuses = BonusCard.objects.order_by("-cost")
    else:
        bonuses = BonusCard.objects.all()

    paginator = Paginator(bonuses, 8)

    return paginator.page(page_num)


def dictionary_preparation(bonuses: list) -> dict:
    """Generate dict, when key it is image base64 and key it is bonus obj."""
    dictionary = {}
    for bonus in bonuses:
        dictionary[bonus] = str(b64encode(bonus.image_binary).decode('ascii'))
    return dictionary
