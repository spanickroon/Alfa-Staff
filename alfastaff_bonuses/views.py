from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def profile(request):
    return render(request, template_name='alfastaff-bonuses/profile.html', context={'user': request.user})


@login_required(login_url='login')
def edit(request):
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