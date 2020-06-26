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
def profile(request):
    return render(
        request, template_name='alfastaff-bonuses/profile.html',
        context={'user': request.user})


@login_required(login_url='login')
def edit(request):
    if request.method == "GET":
        return render(
            request, template_name='alfastaff-bonuses/edit.html',
            context={'user': request.user})


@login_required(login_url='login')
def edit_password(request):
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
def edit_profile(request):
    if request.method == "POST":
        profile_change_form = ProfileChangeForm(request.POST, request.FILES)
        if profile_change_form.is_valid():
            user = User.objects.get(email=request.user.email)
            user.email = profile_change_form.cleaned_data.get('email')

            if profile_change_form.cleaned_data.get('avatar') != "anon_user.png":
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
                context={'user': request.user, 'error': True})
    else:
        return redirect(to="edit")


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return render(
        request, template_name='alfastaff-account/login.html',
        context={'user': request.user})


@login_required(login_url='login')
def purchases(request):
    if request.method == "GET":
        count_page = "".join(map(str, list(
            range(1, math.ceil(len(Purchase.objects.all()) / 10) + 1))))

        return render(
            request, template_name='alfastaff-bonuses/purchases.html',
            context={'user': request.user, 'count_page': count_page})


@login_required(login_url='login')
def purchases_page(request, page=1, sort='sort_date'):
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
def bonuses(request):
    if request.method == "GET":
        count_page = "".join(map(str, list(
            range(1, math.ceil(len(BonusCard.objects.all()) / 8) + 1))))

        return render(
            request, template_name='alfastaff-bonuses/catalog.html',
            context={'user': request.user, 'count_page': count_page})


@login_required(login_url='login')
def bonuses_page(request, page=1, sort='sort_alphabet'):
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
def buy(request, id):
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
                balance=user.profile.points - bonus.cost,
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
        except(TypeError, ValueError, OverflowError, User.DoesNotExist) as ex:
            print(ex)
            return JsonResponse({"buy": "error"})
