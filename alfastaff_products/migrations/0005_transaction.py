# Generated by Django 3.0.7 on 2020-11-18 19:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('alfastaff_products', '0004_auto_20201118_1744'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(blank=True, null=True, verbose_name='Сумма')),
                ('date_replenishment', models.DateField(auto_now=True, null=True, verbose_name='Дата транзакции')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользоваетль')),
            ],
            options={
                'verbose_name': 'Транзакция',
                'verbose_name_plural': 'Транзпкции',
                'ordering': ['-id'],
            },
        ),
    ]
