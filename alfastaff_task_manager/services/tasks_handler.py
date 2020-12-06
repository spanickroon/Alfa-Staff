"""This module contain functions for work with tasks in taskmanager."""

from django.contrib.auth.models import User
from dropbox.files import SharedLink

from alfastaff_shedule.models import ScheduleForOneDay

from ..models import Task


def get_tasks_and_date_for_day(request: object) -> list:
    """get_tasks_and_date_for_day for get all tasks for day."""
    number_day = request.POST.get('number_day')
    tasks = Task.objects.filter(day__number_day=number_day, day__user=request.user)
    schedule_for_one_day = ScheduleForOneDay.objects.get(number_day=number_day, user=request.user)
    select_date = ".".join([
        str(schedule_for_one_day.number_day),
        str(schedule_for_one_day.month),
        str(schedule_for_one_day.year)
        ])
    return select_date, tasks