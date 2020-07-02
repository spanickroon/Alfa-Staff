"""This module contain functions for proccesing requests."""

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import BonusCard, Purchase
from .forms import PasswordChangeForm, ProfileChangeForm

from .services.edit_password_handler import edit_password_processing
from .services.edit_profile_handler import edit_profile_processing
from .services.purchases_page_handler import get_purchases
from .services.bonuses_page_handler import get_bonuses
from .services.buy_handler import buy_processing
from .services.error_handling_decorator import error_handling

import math


@error_handling
@login_required(login_url='login')
def profile(request: object):
    """Profile function processes 1 types of request.

    1. GET
        Returns the reset profile page.
    """
    return render(
        request, template_name='alfastaff-bonuses/profile.html',
        context={'user': request.user})


@error_handling
@login_required(login_url='login')
def edit(request: object):
    """Edit function processes 1 types of request.

    1. GET
        Returns the edit page.
    """
    if request.method == "GET":
        user = User.objects.get(email=request.user.email)

        return render(
            request, template_name='alfastaff-bonuses/edit.html',
            context={'user': user})


@error_handling
@login_required(login_url='login')
def edit_password(request: object):
    """edit_password function processes 2 types of request post and get.

    1. GET
        Redirect to the edit page;
    2. POST
        Checks the validity of the data,
        checks whether the user verifies the passwords for equality;
        if everything is good, then he changes the password and redirects to the page,
        if the error returns it to the page.
    """
    if request.method == "POST":
        password_change_form = PasswordChangeForm(request.POST)

        if password_change_form.is_valid():
            return edit_password_processing(request, password_change_form)
        else:
            return render(
                request, template_name='alfastaff-bonuses/edit.html',
                context={'user': request.user, 'error': True})
    else:
        return redirect(to="edit")


@error_handling
@login_required(login_url='login')
def edit_profile(request: object):
    """edit_profile function processes 2 types of request post and get.

    1. GET
        Redirect to the edit page;
    2. POST
        Checks the validity of the data,
        changes the user’s object fields and checks for the presence of a standard photo,
        saves the user and authorizes him again and then redirects to editing.
    """
    if request.method == "POST":
        profile_change_form = ProfileChangeForm(request.POST, request.FILES)

        if profile_change_form.is_valid():
            return edit_profile_processing(request, profile_change_form)
        else:
            return render(
                request, template_name='alfastaff-bonuses/edit.html',
                context={'user': request.user, 'error_profile': True})
    else:
        return redirect(to="edit")


@error_handling
@login_required(login_url='login')
def logout_user(request: object):
    """logout_user function processes 1 types of request.

    1. GET
        Returns the login page and logout user.
    """
    if request.method == "GET":
        logout(request)
        return render(
            request, template_name='alfastaff-account/login.html',
            context={'user': request.user})


@error_handling
@login_required(login_url='login')
def purchases(request: object):
    """Purchases function processes 1 types of request.

    1. GET
        return number of page on purchases.html
    """
    if request.method == "GET":
        count_page = "".join(map(str, list(
            range(1, math.ceil(len(Purchase.objects.all()) / 10) + 1))))

        return render(
            request, template_name='alfastaff-bonuses/purchases.html',
            context={'user': request.user, 'count_page': count_page})


@error_handling
@login_required(login_url='login')
def purchases_page(request: object, page: int, sort: str):
    """purchases_page function processes 1 types of request.

    1. GET
        It takes several arguments from the query string such as the page number and sort name,
        takes out the elements according to the page and sorts them according to the sort name
        and returns to the page.
    """
    if request.method == "GET":
        purchases = get_purchases(request, page, sort)

        return render(
            request, template_name='alfastaff-bonuses/list_purchases.html',
            context={'purchases': purchases})


@error_handling
@login_required(login_url='login')
def bonuses(request: object):
    """Bonuses function processes 1 types of request.

    1. GET
        return number of page on catalog.html
    """
    if request.method == "GET":
        count_page = "".join(map(str, list(
            range(1, math.ceil(len(BonusCard.objects.all()) / 8) + 1))))

        return render(
            request, template_name='alfastaff-bonuses/catalog.html',
            context={'user': request.user, 'count_page': count_page})


@error_handling
@login_required(login_url='login')
def bonuses_page(request: object, page: int, sort: str):
    """bonuses_page function processes 1 types of request.

    1. GET
        It takes several arguments from the query string such as the page number and sort name,
        takes out the elements according to the page and sorts them according to the sort name
        and returns to the page.
    """
    if request.method == "GET":
        bonuses = get_bonuses(request, page, sort)

        return render(
            request, template_name='alfastaff-bonuses/list_bonuses.html',
            context={'bonuses': bonuses})


@error_handling
@login_required(login_url='login')
def buy(request: object, id: int):
    """bonuses_page function processes 1 types of request.

    1. GET
        We get the goods from the user’s database,
        check whether the purchase is possible and create a new purchase object,
        then save it, after which we send the message about the purchase to the administrator,
        otherwise we return an error in JSON format
    """
    if request.method == "GET":
        return buy_processing(request, id)
