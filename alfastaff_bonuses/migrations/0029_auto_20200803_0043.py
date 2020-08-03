# Generated by Django 3.0.7 on 2020-08-02 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alfastaff_bonuses', '0028_auto_20200729_2227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bonuscard',
            name='image_binary',
        ),
        migrations.AlterField(
            model_name='bonuscard',
            name='image',
            field=models.ImageField(blank=True, default='bonuses/incognita.png', null=True, upload_to='bonuses', verbose_name='Фотография'),
        ),
    ]