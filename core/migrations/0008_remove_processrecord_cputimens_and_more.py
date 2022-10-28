# Generated by Django 4.1.2 on 2022-10-28 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_processrecord_imagename'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='processrecord',
            name='cpuTimeNs',
        ),
        migrations.AddField(
            model_name='processrecord',
            name='cpuClockRate',
            field=models.BigIntegerField(null=True, verbose_name='Частота процессора'),
        ),
        migrations.AddField(
            model_name='processrecord',
            name='cpuCycles',
            field=models.BigIntegerField(null=True, verbose_name='Процессорные циклы'),
        ),
    ]
