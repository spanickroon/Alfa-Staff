# Generated by Django 3.0.7 on 2020-07-29 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alfastaff_shedule', '0002_auto_20200729_2020'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PersonnelLoadTable',
            new_name='PersonnelLoadDocument',
        ),
        migrations.AlterModelOptions(
            name='personnelloaddocument',
            options={'ordering': ['-date_upload'], 'verbose_name': 'Документ нагрузки персонала', 'verbose_name_plural': 'Документы нагрузки персонала'},
        ),
        migrations.AlterModelTable(
            name='personnelloaddocument',
            table='Документы нагрузки персонала',
        ),
    ]