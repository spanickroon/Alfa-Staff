"""This module contain functions for proccesing requests."""

from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from .services.tasks_handler import get_tasks_and_date_for_day


@login_required(login_url='login')
def taskmanager(request: object):
    """Taskmanager function processes 1 types of request.

    1. POST
        Returns the page with tasks.
    """

    if request.method == "POST":
        select_date, tasks = get_tasks_and_date_for_day(request)
        return render(request, template_name='alfastaff-task-manager/taskmanager.html',
            context={'date':select_date, 'tasks': tasks}
        )
