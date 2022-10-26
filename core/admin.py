from django.contrib import admin

import core.models
from core import models
# Register your models here.

@admin.register(core.models.Person)
class Person(admin.ModelAdmin):
    list_display = ('name', 'phone')
    search_fields = ('name', )
    def __str__(self):
        return self.name


@admin.register(core.models.ProcessRecord)
class ProcessRecord(admin.ModelAdmin):
    list_display = ('imagePath', 'osPid', 'timestampBegin', 'timestampEnd', 'cpuTimeNs')
    search_fields = ('imagePath', 'osPid', 'timestampBegin', 'timestampEnd')

    #def __str__(self):
    #Todo: add nice str to ProcessRecord
    #    return [ self.imagePath, self.osPid, self.timesta