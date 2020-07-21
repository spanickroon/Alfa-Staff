"""This module contain Profile class."""

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Profile class with function output and meta data."""

    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
        verbose_name="Пользователь")
    avatar = models.ImageField(
        default="images/profiles/anon_user.png",
        verbose_name="Фотография",
        upload_to='profiles', null=True, blank=True)
    avatar_binary = models.BinaryField(
        verbose_name="Фотография байткод", blank=True, editable=True)
    first_name = models.CharField(
        default="Имя", max_length=30,
        verbose_name="Имя",
        blank=True, null=True)
    second_name = models.CharField(
        default="Фамилия", max_length=30,
        verbose_name="Фамилия",
        blank=True, null=True)
    middle_name = models.CharField(
        default="Отчество", max_length=30,
        verbose_name="Отчество",
        blank=True, null=True)
    number_phone = models.CharField(
        default="Не задано", max_length=15,
        verbose_name="Номер телефона",
        blank=True, null=True)

    STATUS_CHOICES = (
        ('Работает', 'Работает'),
        ('Отпуск', 'Отпуск'),
        ('Больничный', 'Больничный'),
        ('Уволен', 'Уволен')
    )
    status = models.CharField(
        default="Не задано", max_length=15,
        verbose_name="Статус",
        choices=STATUS_CHOICES, blank=True, null=True)

    points = models.IntegerField(
        default=0, blank=True,
        null=True, verbose_name="Бонусы")
    position = models.CharField(
        default="Не задано", max_length=50,
        verbose_name="Должность",
        blank=True, null=True)
    department = models.CharField(
        default="Не задано", max_length=50,
        verbose_name="Отдел",
        blank=True, null=True)

    ROLE_CHOICES = (
        (1, 'Админ'),
        (2, 'Модер'),
        (3, 'Пользователь')
    )
    role = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, blank=True, null=True,
        verbose_name="Роль")

    class Meta:
        """Meta data."""

        db_table = 'Профиль'
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профиль'

    def __str__(self) -> str:
        """Funtion for output info about this profile object."""
        return self.user.email
