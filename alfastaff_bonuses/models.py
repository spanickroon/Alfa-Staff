from django.db import models
from django.contrib.auth.models import User


class BonusCard(models.Model):
    name = models.CharField(max_length=50,  blank=True, null=True)
    description = models.CharField(max_length=100,  blank=True, null=True)
    cost = models.IntegerField(blank=True, null=True)
    image = models.ImageField(default="bonuses/product.jpg", upload_to='bonuses', null=True, blank=True)

    class Meta:
        db_table = 'Товары'
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'
        ordering = ["name"]

    def __str__(self):
        return self.name


class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=50,  blank=True, null=True)
    description = models.CharField(max_length=100,  blank=True, null=True)
    cost = models.IntegerField(blank=True, null=True)
    date_buy = models.DateTimeField(blank=True, null=True)
    balance = models.IntegerField(blank=True, null=True)
    
    STATUS_CHOICES = (
        (1, 'Одобрено'),
        (2, 'Отменено'),
        (3, 'Ожидание')
    )
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, blank=True, null=True)

    class Meta:
        db_table = 'Покупки'
        verbose_name = 'Покупки'
        verbose_name_plural = 'Покупки'

    def __str__(self):
        return self.user