from django.db import models
from django.forms import DateField

# Create your models here.

class Familiar(models.Model):
    name=models.CharField(max_length=40)
    years=models.IntegerField()
    birth=models.DateField()
