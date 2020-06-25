from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def shedule(request):
    return render(request, template_name='alfastaff-shedule/shedule.html', context={'user': request.user})
