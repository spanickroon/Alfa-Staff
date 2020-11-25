"""This module contain with PersonnelLoadDocument and ScheduleForOneDay class."""

import pandas as pd
import csv
import calendar

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from dropbox.files import Metadata


class PersonnelLoadDocument(models.Model):
    """PersonnelLoadDocument class with function output and meta data."""

    name = models.CharField(
        max_length=50, blank=True,
        verbose_name="Название", null=True)
    date_upload = models.DateField(
        auto_now=True, blank=True,
        verbose_name="Дата загрузки", null=True)
    file_with_table = models.FileField(
        blank=True, verbose_name="CSV файл с нагрузкой персонала",
        null=True, upload_to="documents")

    class Meta:
        """Meta data."""

        verbose_name = 'Документ нагрузки персонала'
        verbose_name_plural = 'Документы нагрузки персонала'
        ordering = ["-date_upload"]

    def __str__(self):
        """Funtion for output info about this document object."""
        return "{0} - {1}".format(self.name, self.date_upload)


class ScheduleForOneDay(models.Model):
    """ScheduleForOneDay class with function output and meta data."""

    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name="Пользоваетль")
    day_of_week = models.CharField(
        max_length=15, blank=True,
        verbose_name="День недели", null=True)
    year = models.IntegerField(
        blank=True,
        verbose_name="Год", null=True)

    MONTH_CHOICES = (
        (1, 'Jun'),
        (2, 'Feb'),
        (3, 'Mar'),
        (4, 'Apr'),
        (5, 'May'),
        (6, 'Jun'),
        (7, 'Jul'),
        (8, 'Aug'),
        (9, 'Sep'),
        (10, 'Oct'),
        (11, 'Nov'),
        (12, 'Dec')
    )
    month = models.PositiveSmallIntegerField(
        blank=True, choices=MONTH_CHOICES,
        verbose_name="Месяц", null=True)

    number_day = models.IntegerField(
        blank=True, null=True,
        verbose_name="Номер дня в месяце",)
    working_hours = models.CharField(
        max_length=30, blank=True,
        verbose_name="Время работы", null=True)
    lunch_time = models.CharField(
        max_length=30, blank=True,
        verbose_name="Время обеда", null=True)
    technical_break_time = models.CharField(
        max_length=30, blank=True,
        verbose_name="Время тех. перерыва", null=True)
    holiday = models.BooleanField(
        blank=True,
        verbose_name="Праздник", null=True)
    day_off = models.BooleanField(
        blank=True,
        verbose_name="Выходной", null=True)

    class Meta:
        """Meta data."""

        verbose_name = 'Расписание сотрудника на день'
        verbose_name_plural = 'Расписание сотрудников по дням'
        ordering = ["user"]

    def __str__(self):
        """Funtion for output info about this schedule object."""
        return "{0} {1} {2} - {3}.{4}.{5}".format(
                self.user.profile.second_name,
                self.user.profile.first_name,
                self.user.profile.middle_name,
                self.number_day,
                self.month,
                self.year,
            )


@receiver(post_save, sender=PersonnelLoadDocument)
def create_shedule_for_staff(sender, instance, **kwargs):
    """Create shedule for staff after added csv file."""
    data = pd.read_csv(instance.file_with_table.url)

    for i, row in data.iterrows():
        user = User.objects.get(email=row['email'])

        try:
            ScheduleForOneDay.objects.filter(user=user).delete()
        except Exception:
            pass

        for index in range(0, int(row['count_day'])):
            if index + 1 in map(int, row['holiday'].split(',')):
                holiday = True
            else:
                holiday = False

            name_day = calendar.weekday(row['year'], row['month'], index + 1)
            if name_day == 0:
                name_day = "mon"
            elif name_day == 1:
                name_day = "tue"
            elif name_day == 2:
                name_day = "wed"
            elif name_day == 3:
                name_day = "thu"
            elif name_day == 4:
                name_day = "fri"
            elif name_day == 5:
                name_day = "sat"
            else:
                name_day = "sun"
            
            if name_day == "sun" or name_day == "sat":
                day_off = True
            else:
                day_off = False

            shedule_for_one_day = ScheduleForOneDay(
                user = user,
                day_of_week = name_day,
                year = row['year'],
                month = row['month'],
                number_day = index + 1,
                working_hours = row['working_hours'],
                lunch_time = row['lunch_time'],
                technical_break_time = row['technical_break_time'],
                holiday = holiday,
                day_off = day_off
            )
            shedule_for_one_day.save()
