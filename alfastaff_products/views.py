"""This module contain functions for proccesing requests."""

from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from .forms import PasswordChangeForm, ProfileChangeForm

from .services.edit_password_handler import edit_password_processing
from .services.edit_profile_handler import edit_profile_processing
from .services.purchases_page_handler import get_purchases
from .services.products_page_handler import get_products
from .services.buy_handler import buy_processing
from .services.count_page_handler import count_page_products, count_page_purchases
from .services.top_up_account_handler import top_up_account_processing


@login_required(login_url='login')
def profile(request: object):
    """Profile function processes 1 types of request.

    1. GET
        Returns the reset profile page.
    """
    if request.method == "GET":
        return render(
            request, template_name='alfastaff-products/profile.html',
            context={'user': request.user, 'avatar': request.user.profile.avatar.url})


@login_required(login_url='login')
def edit(request: object):
    """Edit function processes 1 types of request.

    1. GET
        Returns the edit page.
    """
    if request.method == "GET":
        return render(
            request, template_name='alfastaff-products/edit.html',
            context={'user': request.user, 'avatar': request.user.profile.avatar.url})


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
                request, template_name='alfastaff-products/edit.html',
                context={'user': request.user, 'error': True, 'avatar': request.user.profile.avatar.url})
    else:
        return redirect(to="edit")


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
                request, template_name='alfastaff-products/edit.html',
                context={'user': request.user, 'error_profile': True})
    else:
        return redirect(to="edit")


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


@login_required(login_url='login')
def purchases(request: object):
    """Purchases function processes 1 types of request.

    1. GET
        return number of page on purchases.html
    """
    if request.method == "GET":
        count_page = count_page_purchases(request)

        return render(
            request, template_name='alfastaff-products/purchases.html',
            context={'user': request.user, 'count_page': count_page})


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
            request, template_name='alfastaff-products/list_purchases.html',
            context={'purchases': purchases})


@login_required(login_url='login')
def products(request: object):
    """Product function processes 1 types of request.

    1. GET
        return number of page on catalog.html
    """
    if request.method == "GET":
        count_page = count_page_products()

        return render(
            request, template_name='alfastaff-products/catalog.html',
            context={'user': request.user, 'count_page': count_page})


@login_required(login_url='login')
def products_page(request: object, page: int, sort: str):
    """products_page function processes 1 types of request.

    1. GET
        It takes several arguments from the query string such as the page number and sort name,
        takes out the elements according to the page and sorts them according to the sort name
        and returns to the page.
    """
    if request.method == "GET":
        products = get_products(request, page, sort)

        return render(
            request, template_name='alfastaff-products/list_products.html',
            context={'products': products})


@login_required(login_url='login')
def buy(request: object, id: int):
    """buy function processes 1 types of request.

    1. GET
        We get the goods from the user’s database,
        check whether the purchase is possible and create a new purchase object,
        then save it, after which we send the message about the purchase to the administrator,
        otherwise we return an error in JSON format
    """
    if request.method == "GET":
        return buy_processing(request, id)


@login_required(login_url='login')
def top_up_account(request: object):
    """top up an account function processes 1 types of request.

    1. POST
    """
    if request.method == "POST":
        return top_up_account_processing(request)