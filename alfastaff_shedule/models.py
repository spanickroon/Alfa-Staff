"""This module contain with PersonnelLoadDocument and ScheduleForOneDay class."""

from django.db import models
from django.contrib.auth.models import User


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
        (3, 'Mar')
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
