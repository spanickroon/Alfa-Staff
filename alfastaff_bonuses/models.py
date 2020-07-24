"""This module contain BonusCard and Purchase class."""

from django.db import models
from django.contrib.auth.models import User


class BonusCard(models.Model):
    """BonusCard class with function output and meta data."""

    name = models.CharField(
        max_length=50, blank=True,
        verbose_name="Название", null=True)
    image_binary = models.BinaryField(
        verbose_name="Фотография байткод", blank=True, editable=False)
    cost = models.IntegerField(
        blank=True, null=True, verbose_name="Стоимость")
    image = models.ImageField(
        default="images/bonuses/incognita.png", upload_to='bonuses',
        null=True, blank=True, verbose_name="Фотография")

    class Meta:
        """Meta data."""

        db_table = 'Товары'
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'
        ordering = ["name"]

    def __str__(self):
        """Funtion for output info about this bonuses card object."""
        return self.name


class Purchase(models.Model):
    """Purchase class with function output and meta data."""

    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name="Пользоваетль")
    name = models.CharField(
        max_length=50, blank=True,
        verbose_name="Название товара", null=True)
    id_purchase = models.IntegerField(
        blank=True, null=True,
        verbose_name="ID",)
    cost = models.IntegerField(
        blank=True, null=True,
        verbose_name="Стоимость товара")
    date_buy = models.DateField(
        auto_now=True, blank=True,
        verbose_name="Дата покупки", null=True)
    balance = models.IntegerField(
        blank=True, null=True,
        verbose_name="Остаток")

    STATUS_CHOICES = (
        (1, 'Одобрено'),
        (2, 'Отменено'),
        (3, 'Ожидание')
    )
    status = models.PositiveSmallIntegerField(
        choices=STATUS_CHOICES, blank=True,
        verbose_name="Статус", null=True)

    class Meta:
        """Meta data."""

        db_table = 'Покупки'
        verbose_name = 'Покупки'
        verbose_name_plural = 'Покупки'
        ordering = ["-id"]

    def __str__(self):
        """Funtion for output info about this purchase object."""
        return "{0} {1} {2} - {3}".format(
                self.user.profile.first_name,
                self.user.profile.second_name,
                self.user.profile.middle_name,
                self.name
            )
