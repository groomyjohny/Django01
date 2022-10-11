from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField('Имя', max_length=255)
    phone = models.IntegerField('Номер телефона')