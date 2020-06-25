from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default="profiles/anon_user.png", upload_to='profiles', null=True, blank=True)
    first_name = models.CharField(default="Имя", max_length=30,  blank=True, null=True)
    second_name = models.CharField(default="Фамилия", max_length=30,  blank=True, null=True)
    middle_name = models.CharField(default="Отчество", max_length=30,  blank=True, null=True)
    number_phone = models.CharField(default="Не задано", max_length=15,  blank=True, null=True)
    
    STATUS_CHOICES = (
        ('Работает', 'Работает'),
        ('Отпуск', 'Отпуск'),
        ('Больничный', 'Больничный'),
        ('Уволен', 'Уволен')
    )
    status = models.CharField(default="Не задано", max_length=15, choices=STATUS_CHOICES, blank=True, null=True)

    points = models.IntegerField(default=0, blank=True, null=True)
    position = models.CharField(default="Не задано", max_length=50,  blank=True, null=True)
    department = models.CharField(default="Не задано", max_length=50,  blank=True, null=True)

    ROLE_CHOICES = (
        (1, 'Админ'),
        (2, 'Модер'),
        (3, 'Пользователь')
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)

    class Meta:
        db_table = 'Профиль'
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профиль'

    def __str__(self):
        return self.user.email
