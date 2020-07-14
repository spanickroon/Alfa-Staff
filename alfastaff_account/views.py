"""This module contain functions for proccesing requests."""

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from .forms import LoginForm, SignupForm, ResetPasswordForm

from .services.email_sender import send_message_with_new_password
from .services.login_handler import login_processing
from .services.signup_handler import signup_processing
from .services.activate_handler import activate_processing
from .services.reset_password_handler import reset_password_processing


def login_user(request: object):
    """login_user function processes 2 types of request post and get.

    1. GET
        If the user is logged in then redirects the profile to the page;
        otherwise, returns the login page.
    2. POST
        Checks the validity of the data and the existence of the user in the database;
        if successful, authorizes the user otherwise, returns a JSON error.
    """
    if request.method == "POST":
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            return login_processing(request, login_form)
        else:
            return JsonResponse({"validation": "error"})
    else:
        if request.user.is_authenticated:
            return redirect(to='profile')

        login_form = LoginForm()
        return render(
            request, template_name='alfastaff-account/login.html',
            context={'login_form': login_form})


def signup_user(request: object):
    """signup_user function processes 2 types of request post and get.

    1. GET
        Returns the login page.
    2. POST
        Checks the accuracy of the data and the absence of the user in the database;
        in case of success,
        Adds the user to the profile database and sends an e-mail with a unique hash value,
        authorizes the user otherwise, returns a JSON error.
    """
    if request.method == "POST":
        signup_form = SignupForm(request.POST)

        if signup_form.is_valid():
            return signup_processing(request, signup_form)
        else:
            return JsonResponse({"confirmation": "error"})
    else:
        login_form = LoginForm()
        return render(
            request, template_name='alfastaff-account/login.html',
            context={'login_form': login_form})


def signup_user_insert(request: object):
    """signup_user_insert function processes 1 types of request.

    1. GET
        Returns the singup form.
    """
    signup_form = SignupForm()
    return render(
        request, template_name='alfastaff-account/signup.html',
        context={'signup_form': signup_form})


def reset_password(request: object):
    """reset_password function processes 2 types of request post and get.

    1. GET
        Returns the login page.
    2. POST
        Checks the accuracy of the data and the absence of the user in the database;
        in case of success,
        Adds the user to the profile database and sends an e-mail with a unique hash value,
        authorizes the user otherwise, returns a JSON error.
    """
    if request.method == "POST":
        reset_password_form = ResetPasswordForm(request.POST)

        if reset_password_form.is_valid():
            return reset_password_processing(request, reset_password_form)
        else:
            return JsonResponse({"reseting": "error"})
    else:
        login_form = LoginForm()
        return render(
            request, template_name='alfastaff-account/login.html',
            context={'login_form': login_form})


def reset_password_insert(request: object):
    """reset_password_insert function processes 1 types of request.

    1. GET
        Returns the reset password form.
    """
    reset_password_form = ResetPasswordForm()
    return render(
        request, template_name='alfastaff-account/reset_password.html',
        context={'reset_password_form': reset_password_form})


def activate_user(request: object, uidb64: str, token: str):
    """activate_user function processes 1 types of request.

    1. GET
        Decodes the link that the user came to,
        compares the hash of the user and the token,
        and after successful execution,
        authorizes the user and activates the account status as confirmed
        and redirect on profile page.
    """
    flag = activate_processing(request, uidb64, token)

    if flag:
        return redirect('profile')
    else:
        return render(request, template_name='alfastaff-account/activate_error.html')
