"""This module contain class for work with PersonnelLoadDocument and ScheduleForOneDay object in admin panel."""

from django.contrib import admin

from .models import PersonnelLoadDocument, ScheduleForOneDay


@admin.register(PersonnelLoadDocument)
class AuthorAdmin(admin.ModelAdmin):
    """PersonnelLoadDocument class with list of filters."""

    list_filter = ('name', 'date_upload',)


@admin.register(ScheduleForOneDay)
class AuthorAdmin(admin.ModelAdmin):
    """ScheduleForOneDay class with list of filters."""

    list_filter = ('day_of_week', 'year', 'month', 'number_day',)