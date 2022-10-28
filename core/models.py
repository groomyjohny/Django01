from django.db import models
import os
# Create your models here.
class ProcessRecord(models.Model):
    imageName = models.CharField('Процесс', max_length=512)
    imagePath = models.CharField('Путь к файлу', max_length=512)
    osPid = models.BigIntegerField('PID')
    osParentPid = models.BigIntegerField('PID родителя', blank=True, null=True)
    timestampBegin = models.DateTimeField('Время начала')
    timestampEnd = models.DateTimeField('Время конца')
    cpuCycles = models.BigIntegerField("Процессорные циклы", null=True)
    cpuClockRate = models.BigIntegerField("Частота процессора", null=True)

    @property
    def cpuTimeNs(self):
        try:
            return (self.cpuCycles * 1000000000) // self.cpuClockRate
        except TypeError:
            return 0

    def getImageName(self):
        fileName = os.path.basename(self.imagePath)
        fileNameWithExtension = os.path.splitext(fileName)
        return ''.join(fileNameWithExtension) #dot not required, extension already contains it

    def fromDict(self, d):
        imageName = d['imageName'],
        imagePath = d['imagePath'],
        osPid = d['osPid'],
        osParentPid = d['osParentPid'],
        timestampBegin = d['timestampBegin'],
        timestampEnd = d['timestampEnd'],
        cpuTimeNs = (int(d['cycles']) * 1000000000) // int(d['clockRate'])
        pass

    def toDict(self):
        return {
            'id': self.id,
            'imageName': self.imageName,
            'imagePath': self.imagePath,
            'osPid': self.osPid,
            'osParentPid': self.osParentPid,
            'timestampBegin': self.timestampBegin,
            'timestampEnd': self.timestampEnd,
            'cpuTimeNs': self.cpuTimeNs,
        }