from django.http import HttpResponse
from django.shortcuts import render

from .models import Profile
from .tokens import *
from .forms import LoginForm, SignupForm


def login(request):
    return render(request, template_name='alfastaff/account/login.html')
