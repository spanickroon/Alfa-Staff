from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

from .models import Profile
from .tokens import account_activation_token
from .forms import LoginForm, SignupForm


def login_user(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = User.objects.get(email=login_form.cleaned_data["email"], password=login_form.cleaned_data["password"])
            login(request, user)
            return JsonResponse({"validation": "ok"})
        else:
            login_form = LoginForm()
            return render(request, template_name='alfastaff-account/login.html', context={'login_form': login_form})
    else:
        login_form = LoginForm()
        return render(request, template_name='alfastaff-account/login.html', context={'login_form': login_form})


def signup_user(request):
    if request.method == "POST":
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            user = User(
                username=signup_form.cleaned_data['email'],
                email=signup_form.cleaned_data['email'],
                password=signup_form.cleaned_data['password1']
            )
            user.is_active = True
            user.save()
            profile = Profile(
                user=user
            )
            profile.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
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
            login_form = LoginForm()
            return render(request, template_name='alfastaff-account/login.html', context={'login_form': login_form})
    else:
        login_form = LoginForm()
        return render(request, template_name='alfastaff-account/login.html', context={'login_form': login_form})


def signup_user_insert(request):
    signup_form = SignupForm()
    return render(request, template_name='alfastaff-account/signup.html', context={'signup_form': signup_form})


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
        return render(request, template_name='alfastaff-account/activate_error.html')


def logout_user(request):
    logout(request)
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return render(request, template_name='alfastaff-account/logout.html')
