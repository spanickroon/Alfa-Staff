from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.base_user import BaseUserManager

from .models import Profile
from .tokens import account_activation_token
from .forms import LoginForm, SignupForm, ResetPasswordForm


def login_user(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            try:
                user = User.objects.get(email=login_form.cleaned_data["email"])
                if not check_password(login_form.cleaned_data["password"], user.password):
                    raise ValueError
                login(request, user)
                return JsonResponse({"validation": "ok"})
            except(TypeError, ValueError, OverflowError, User.DoesNotExist):
                return JsonResponse({"validation": "user_not_found"})
        else:
            return JsonResponse({"validation": "error"})
    else:
        if request.user.is_authenticated:
            return redirect(to='profile')
        login_form = LoginForm()
        return render(
            request, template_name='alfastaff-account/login.html',
            context={'login_form': login_form})


def signup_user(request):
    if request.method == "POST":
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            try:
                user = User.objects.get(email=signup_form.cleaned_data["email"])
                return JsonResponse({"confirmation": "user_found"})
            except Exception:
                pass
            user = User(
                username=signup_form.cleaned_data['email'],
                email=signup_form.cleaned_data['email'],
                password=make_password(signup_form.cleaned_data['password1'])
            )
            user.is_active = True
            user.save()
            profile = Profile(
                user=user
            )
            profile.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('alfastaff-account/email_message.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = user.email
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return JsonResponse({"confirmation": "ok"})
        else:
            return JsonResponse({"confirmation": "error"})
    else:
        login_form = LoginForm()
        return render(
            request, template_name='alfastaff-account/login.html',
            context={'login_form': login_form})


def signup_user_insert(request):
    signup_form = SignupForm()
    return render(
        request, template_name='alfastaff-account/signup.html',
        context={'signup_form': signup_form})


def reset_password(request):
    if request.method == "POST":
        reset_password_form = ResetPasswordForm(request.POST)
        if reset_password_form.is_valid():
            try:
                user = User.objects.get(email=reset_password_form.cleaned_data["email"])
            except(TypeError, ValueError, OverflowError, User.DoesNotExist):
                return JsonResponse({"reseting": "user_not_found"})
            new_password = BaseUserManager().make_random_password()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('alfastaff-account/reset_message.html', {
                'user': user,
                'domain': current_site.domain,
                'new_password': new_password
            })
            to_email = user.email
            user.password = make_password(new_password)
            user.save()
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return JsonResponse({"reseting": "ok"})
        else:
            return JsonResponse({"reseting": "error"})
    else:
        login_form = LoginForm()
        return render(
            request, template_name='alfastaff-account/login.html',
            context={'login_form': login_form})


def reset_password_insert(request):
    reset_password_form = ResetPasswordForm()
    return render(
        request, template_name='alfastaff-account/reset_password.html',
        context={'reset_password_form': reset_password_form})


def activate_user(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('profile')
    else:
        return render(
            request, template_name='alfastaff-account/activate_error.html')
