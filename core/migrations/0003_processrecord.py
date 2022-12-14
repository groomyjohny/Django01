# Generated by Django 4.1.2 on 2022-10-26 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_person_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProcessRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagePath', models.CharField(max_length=512, verbose_name='Путь к файлу')),
                ('osPid', models.IntegerField(verbose_name='PID')),
                ('timeBegin', models.DateTimeField(verbose_name='Время начала')),
                ('timeEnd', models.DateTimeField(verbose_name='Время конца')),
                ('cpuCycles', models.BigIntegerField(verbose_name='Циклы процессора')),
            ],
        ),
    ]
