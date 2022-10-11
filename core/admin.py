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