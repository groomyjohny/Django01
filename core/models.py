from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField('Имя', max_length=255)
    phone = models.IntegerField('Номер телефона')

class ProcessRecord(models.Model):
    imagePath = models.CharField('Путь к файлу', max_length=512)
    osPid = models.IntegerField('PID')
    timestampBegin = models.DateTimeField('Время начала')
    timestampEnd = models.DateTimeField('Время конца')
    cpuTimeNs = models.BigIntegerField("Процессорное время (нс)", null=True)