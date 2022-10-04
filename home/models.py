from pyexpat import model
from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length = 30)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateTimeField()
    fav_animal = models.CharField(max_length = 30)
    parentesco = models.CharField(max_length = 30)