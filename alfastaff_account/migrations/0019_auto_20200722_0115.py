# Generated by Django 3.0.7 on 2020-07-21 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alfastaff_account', '0018_auto_20200720_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='images/profiles/anon_user.png', null=True, upload_to='profiles', verbose_name='Фотография'),
        ),
    ]