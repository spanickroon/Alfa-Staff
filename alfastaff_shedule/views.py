"""This module contain functions for proccesing requests."""

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .services.send_review_handler import send_review_processing
from .services.shedule_handler import get_shedule_for_user


@login_required(login_url='login')
def shedule(request: object):
    """Shedule function processes 1 types of request.

    1. GET
        Returns the reset shedule page.
    """
    if request.method == "GET":
        shedule = get_shedule_for_user(request)
        return render(request, template_name='alfastaff-shedule/shedule.html', context={'user': request.user, 'shedule': shedule})


@login_required(login_url='login')
def review(request: object):
    """Review function.

    1. POST
        Send email with review on admin email
    """
    if request.method == "POST":
        return send_review_processing(request)
