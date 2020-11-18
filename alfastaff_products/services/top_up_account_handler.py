"""This module contain functions for buy product on catalog."""

from django.shortcuts import redirect
from django.contrib.auth.models import User

from cloudipsp import Api, Checkout


def top_up_account_processing(request: object) -> object:
    """Buy ptodunct and send message on email admin."""
    try:
        user = User.objects.get(email=request.user.email)

        sum_num = int(request.POST.get('sum'))

        if sum_num > 0:

            api = Api(merchant_id=1396424,
                    secret_key='test')
            checkout = Checkout(api=api)
            data = {
                "currency": "USD",
                "amount": str(sum_num) + '00'
            }
            url = checkout.url(data).get('checkout_url')

            user.profile.money += sum_num
            user.profile.save()

            return redirect(url)
        else:
            return redirect(to="edit")
    except (TypeError, ValueError, OverflowError, User.DoesNotExist) as ex:
        print(ex)
        return redirect(to="edit")
