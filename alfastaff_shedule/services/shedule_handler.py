"""This module contain functions for bonuses page."""

import calendar

from ..models import ScheduleForOneDay


def get_shedule_for_user(request: object) -> list:
    shedule = list(ScheduleForOneDay.objects.filter(user=request.user))
    first_day = shedule[0]
    if first_day.day_of_week == "mon":
        pass
    elif first_day.day_of_week == "tue":
        shedule.insert(0, None)
    elif first_day.day_of_week == "wed":
        for _ in range(0, 2):
            shedule.insert(0, None)
    elif first_day.day_of_week == "thu":
        for _ in range(0, 3):
            shedule.insert(0, None)
    elif first_day.day_of_week == "fri":
        for _ in range(0, 4):
            shedule.insert(0, None)
    elif first_day.day_of_week == "sat":
        for _ in range(0, 5):
            shedule.insert(0, None)
    else:
        for _ in range(0, 6):
            shedule.insert(0, None)
    for _ in range(0, 35 - len(shedule) + 1):
        shedule.append(None)
    return shedule