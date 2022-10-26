from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField('Имя', max_length=255)
    phone = models.IntegerField('Номер телефона')

class ProcessRecord(models.Model):
    imagePath = models.CharField('Путь к файлу', max_length=512)
    osPid = models.IntegerField('PID')
    timeBegin = models.DateTimeField('Время начала')
    timeEnd = models.DateTimeField('Время конца')
    cpuCycles = models.BigIntegerField("Циклы процессора")