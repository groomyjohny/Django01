from django.db import models
import os
# Create your models here.
class ProcessRecord(models.Model):
    imagePath = models.CharField('Путь к файлу', max_length=512)
    osPid = models.BigIntegerField('PID')
    osParentPid = models.BigIntegerField('PID родителя', blank=True, null=True)
    timestampBegin = models.DateTimeField('Время начала')
    timestampEnd = models.DateTimeField('Время конца')
    cpuTimeNs = models.BigIntegerField("Процессорное время (нс)", null=True)

    def getImageName(self):
        fileName = os.path.basename(self.imagePath)
        fileNameWithExtension = os.path.splitext(fileName)
        return ''.join(fileNameWithExtension) #dot not required, extension already contains it