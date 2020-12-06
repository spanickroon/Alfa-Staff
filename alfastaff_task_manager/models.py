"""This module contain Task class."""

from django.db import models
from alfastaff_shedule.models import ScheduleForOneDay


class Task(models.Model):
    """Task class with function output and meta data."""

    day = models.ForeignKey(
        ScheduleForOneDay, on_delete=models.CASCADE,
        verbose_name="День")
    description = models.CharField(
        max_length=1000, blank=True,
        verbose_name="Описание", null=True)

    STATUS_CHOICES = (
        ('К работе', 'К работе'),
        ('В процессе', 'В процессе'),
        ('Готово', 'Готово')
    )
    status = models.CharField(
        max_length=15, verbose_name="Статус",
        choices=STATUS_CHOICES, blank=True, null=True)

    class Meta:
        """Meta data."""

        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ["day"]

    def __str__(self):
        """Funtion for output info about this task object."""
        return "{0} {1} {2} - {3}".format(
                self.day.number_day,
                self.day.month,
                self.day.year,
                self.status
            )