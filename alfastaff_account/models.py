from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, blank=True)
    first_name = models.CharField(max_length=30,  blank=True, null=True)
    second_name = models.CharField(max_length=30,  blank=True, null=True)
    middle_name = models.CharField(max_length=30,  blank=True, null=True)
    number_phone = models.CharField(max_length=15,  blank=True, null=True)
    
    STATUS_CHOICES = (
        (1, 'Работает'),
        (2, 'Отпуск'),
        (3, 'Больничный'),
        (4, 'Уволен')
    )
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, blank=True, null=True)

    points = models.IntegerField(blank=True, null=True)
    position = models.CharField(max_length=50,  blank=True, null=True)
    department = models.CharField(max_length=50,  blank=True, null=True)

    ROLE_CHOICES = (
        (1, 'Админ'),
        (2, 'Модер'),
        (3, 'Пользователь')
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
