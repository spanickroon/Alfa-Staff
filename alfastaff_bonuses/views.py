from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import logout, login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.decorators import login_required

from .forms import PasswordChangeForm, ProfileChangeForm

@login_required(login_url='login')
def profile(request):
    return render(request, template_name='alfastaff-bonuses/profile.html', context={'user': request.user})


@login_required(login_url='login')
def edit(request):
    if request.method == "GET":
        return render(request, template_name='alfastaff-bonuses/edit.html', context={'user': request.user})


@login_required(login_url='login')
def edit_password(request):
    if request.method == "POST":
        password_change_form = PasswordChangeForm(request.POST)
        if password_change_form.is_valid():
            user = User.objects.get(email=request.user.email)
            password1 = password_change_form.cleaned_data.get("password1")
            password2 = password_change_form.cleaned_data.get("password2")
            if password1 and password2 and password1 != password2:
                return render(request, template_name='alfastaff-bonuses/edit.html', context={'user': request.user, 'error': True})
            user.password = make_password(password2)
            user.save()
            login(request, user)
            return redirect(to="edit")
        else:
            return render(request, template_name='alfastaff-bonuses/edit.html', context={'user': request.user, 'error': True})
    else:
        return redirect(to="edit")


@login_required(login_url='login')
def edit_profile(request):
    if request.method == "POST":
        return render(request, template_name='alfastaff-bonuses/edit.html', context={'user': request.user})


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return render(request, template_name='alfastaff-account/login.html', context={'user': request.user})


@login_required(login_url='login')
def list_purchese(request):
    return render(request, template_name='alfastaff-bonuses/list_purchese.html', context={'user': request.user})


@login_required(login_url='login')
def bonuses(request):
    return render(request, template_name='alfastaff-bonuses/bonuses.html', context={'user': request.user})