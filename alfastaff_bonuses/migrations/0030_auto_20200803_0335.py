# Generated by Django 3.0.7 on 2020-08-03 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alfastaff_bonuses', '0029_auto_20200803_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bonuscard',
            name='image',
            field=models.ImageField(blank=True, default='bonuses/product.png', null=True, upload_to='media/bonuses', verbose_name='Фотография'),
        ),
    ]
