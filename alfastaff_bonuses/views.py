"""This module contain functions for proccesing requests."""

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import logout, login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings

from .models import BonusCard, Purchase
from .forms import PasswordChangeForm, ProfileChangeForm

import math


@login_required(login_url='login')
def profile(request: object):
    """Profile function processes 1 types of request.

    1. GET
        Returns the reset profile page.
    """
    return render(
        request, template_name='alfastaff-bonuses/profile.html',
        context={'user': request.user})


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
            user = User.objects.get(email=request.user.email)

            password1 = password_change_form.cleaned_data.get("password1")
            password2 = password_change_form.cleaned_data.get("password2")

            if password1 and password2 and password1 != password2:
                return render(
                    request, template_name='alfastaff-bonuses/edit.html',
                    context={'user': request.user, 'error': True})

            user.password = make_password(password2)
            user.save()

            login(request, user)
            return redirect(to="edit")
        else:
            return render(
                request, template_name='alfastaff-bonuses/edit.html',
                context={'user': request.user, 'error': True})
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
            user = User.objects.get(email=request.user.email)
            user.email = profile_change_form.cleaned_data.get('email')

            if profile_change_form.cleaned_data.get('avatar') != "profiles/anon_user.png":
                user.profile.avatar = profile_change_form.cleaned_data.get('avatar')

            user.profile.first_name = profile_change_form.cleaned_data.get('first_name')
            user.profile.second_name = profile_change_form.cleaned_data.get('second_name')
            user.profile.middle_name = profile_change_form.cleaned_data.get('middle_name')
            user.profile.number_phone = profile_change_form.cleaned_data.get('number_phone')
            user.profile.position = profile_change_form.cleaned_data.get('position')
            user.profile.department = profile_change_form.cleaned_data.get('department')

            user.profile.save()
            user.save()

            login(request, user)
            return redirect(to="edit")
        else:
            return render(
                request, template_name='alfastaff-bonuses/edit.html',
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
        count_page = "".join(map(str, list(
            range(1, math.ceil(len(Purchase.objects.all()) / 10) + 1))))

        return render(
            request, template_name='alfastaff-bonuses/purchases.html',
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
        if sort == "sort_cost":
            purchases = Purchase.objects.filter(user=request.user).order_by("-cost")
        else:
            purchases = Purchase.objects.filter(user=request.user)

        if (page * 10) - 10 >= len(purchases):
            purchases = purchases[(len(purchases) // 10) * 10:len(purchases)]
        else:
            if len(purchases) > 10 and len(purchases) % 8 == 0:
                purchases = purchases[(10 * page) - 10:(10 * page)]
            elif len(purchases) > 10 and len(purchases) % 10 != 0:
                if (10 * page) < len(purchases):
                    purchases = purchases[(10 * page) - 10:(10 * page)]
                else:
                    purchases = purchases[(10 * page) - 10:len(purchases)]

        return render(
            request, template_name='alfastaff-bonuses/list_purchases.html',
            context={'purchases': purchases})


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


@login_required(login_url='login')
def bonuses_page(request: object, page: int, sort: str):
    """bonuses_page function processes 1 types of request.

    1. GET
        It takes several arguments from the query string such as the page number and sort name,
        takes out the elements according to the page and sorts them according to the sort name
        and returns to the page.
    """
    if request.method == "GET":
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

        return render(
            request, template_name='alfastaff-bonuses/list_bonuses.html',
            context={'bonuses': bonuses})


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
        try:
            user = User.objects.get(email=request.user.email)
            bonus = BonusCard.objects.get(id=id)

            if user.profile.points - bonus.cost < 0:
                return JsonResponse({"buy": "not_points"})

            user.profile.points = user.profile.points - bonus.cost
            user.profile.save()

            purchase = Purchase(
                user=user,
                name=bonus.name,
                id_purchase=len(Purchase.objects.filter(user=request.user)) + 1,
                cost=bonus.cost,
                balance=user.profile.points,
                status=3
            )
            purchase.save()

            current_site = get_current_site(request)
            mail_subject = 'Buy bonuses.'
            message = render_to_string('alfastaff-bonuses/buy_message.html', {
                'user': user,
                'domain': current_site.domain,
            })
            to_email = settings.EMAIL_HOST_USER
            email = EmailMessage(mail_subject, message, to=[to_email])

            email.send()
            return JsonResponse({"buy": "ok"})
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return JsonResponse({"buy": "error"})
