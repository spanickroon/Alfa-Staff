from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def profile(request):
    return render(request, template_name='alfastaff-bonuses/profile.html')