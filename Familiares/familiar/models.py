from django.db import models

# Create your models here.
class Familiares(models.Model):
    name = models.CharField (max_length= 40)
    apellido = models.CharField (max_length=40)
    edad = models.FloatField(max_length=3)
    dni = models.CharField(max_length= 20)
    fecha_cumpleanios = models.CharField(max_length=20)