from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Profile
from .tokens import TokenGenerator
from .forms import LoginForm, SignupForm


def login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            return HttpResponse("<h2>Козинак как обычно - якорь, иди верстай страницы.</h2>")
        else:
            return HttpResponse("Invalid data")
    else:
        login_form = LoginForm()
        return render(request, template_name='alfastaff-account/login.html', context={'login_form': login_form})

def signup(request):
    if request.method == "POST":
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            return HttpResponse("<h2>Козинак как обычно - якорь, иди верстай страницы.</h2>")
        else:
            return HttpResponse("Invalid data")
    else:
        signup_form = SignupForm()
        return render(request, template_name='alfastaff-account/signup.html', context={'signup_form': signup_form})

def logout(request):
    logout(request)
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return render(request, template_name='alfastaff-account/logout.html')
