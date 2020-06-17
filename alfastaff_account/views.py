from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth.models import User

from .models import Profile
from .tokens import account_activation_token
from .forms import LoginForm, SignupForm


def login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = User.objects.get(email=userform.cleaned_data["email"])
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"error": True})
    else:
        login_form = LoginForm()
        return render(
            request, template_name='alfastaff-account/login.html',
            context={'login_form': login_form})


def signup(request):
    if request.method == "POST":
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save(commit=False)
            user.is_active = False
            user.username = user.email
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
            return render(request, template_name='alfastaff-account/confirm_email.html')
        else:
            return render(
                request, template_name='alfastaff-account/signup.html',
                context={'signup_form': signup_form})
    else:
        signup_form = SignupForm()
        return render(
            request, template_name='alfastaff-account/signup.html',
            context={'signup_form': signup_form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return render(request, template_name='alfastaff-account/confirmation.html')
    else:
        return render(request, template_name='alfastaff-account/active_error.html')


def logout(request):
    logout(request)
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return render(request, template_name='alfastaff-account/logout.html')
