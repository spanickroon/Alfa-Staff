"""This module contain ProductCard and Purchase class."""

from django.db import models
from django.contrib.auth.models import User


class ProductCard(models.Model):
    """ProductCard class with function output and meta data."""

    name = models.CharField(
        max_length=50, blank=True,
        verbose_name='Название', null=True)
    cost = models.IntegerField(
        blank=True, null=True, verbose_name='Стоимость')
    image = models.ImageField(
        default='images/products/product.jpg', upload_to='images/products',
        null=True, blank=True, verbose_name="Фото")

    class Meta:
        """Meta data."""

        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ["name"]

    def __str__(self):
        """Funtion for output info about this products card object."""
        return self.name


class Purchase(models.Model):
    """Purchase class with function output and meta data."""

    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name="Пользоваетль")
    name = models.CharField(
        max_length=50, blank=True,
        verbose_name="Название продукта", null=True)
    id_purchase = models.IntegerField(
        blank=True, null=True,
        verbose_name="ID",)
    cost = models.IntegerField(
        blank=True, null=True,
        verbose_name="Стоимость продукта")
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

        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'
        ordering = ["-id"]

    def __str__(self):
        """Funtion for output info about this purchase object."""
        return "{0} {1} {2} - {3}".format(
                self.user.profile.second_name,
                self.user.profile.first_name,
                self.user.profile.middle_name,
                self.name
            )
