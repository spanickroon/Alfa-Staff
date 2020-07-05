"""This module contain functions for proccesing requests."""

from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def shedule(request: object):
    """Shedule function processes 1 types of request.

    1. GET
        Returns the reset shedule page.
    """
    return render(request, template_name='alfastaff-shedule/shedule.html', context={'user': request.user})
