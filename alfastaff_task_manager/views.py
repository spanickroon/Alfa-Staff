from django.shortcuts import render

from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def taskmanager(request: object):

    if request.method == "GET":
        return render(request, template_name='alfastaff-task-manager/taskmanager.html')
