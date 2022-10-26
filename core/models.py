from django.db import models

# Create your models here.
class ProcessRecord(models.Model):
    imagePath = models.CharField('Путь к файлу', max_length=512)
    osPid = models.IntegerField('PID')
    timestampBegin = models.DateTimeField('Время начала')
    timestampEnd = models.DateTimeField('Время конца')
    cpuTimeNs = models.BigIntegerField("Процессорное время (нс)", null=True)