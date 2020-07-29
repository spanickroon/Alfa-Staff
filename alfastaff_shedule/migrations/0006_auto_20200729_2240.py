# Generated by Django 3.0.7 on 2020-07-29 19:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('alfastaff_shedule', '0005_auto_20200729_2228'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DailySchedule',
            new_name='ScheduleForOneDay',
        ),
        migrations.AlterModelOptions(
            name='scheduleforoneday',
            options={'ordering': ['user'], 'verbose_name': 'Расписание сотрудника на день', 'verbose_name_plural': 'Расписание сотрудников по дням'},
        ),
    ]