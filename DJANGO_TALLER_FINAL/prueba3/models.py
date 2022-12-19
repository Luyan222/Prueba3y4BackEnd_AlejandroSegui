from unittest.util import _MAX_LENGTH
from django.db import models
from .elecciones import elecciones


class Institucion(models.Model):
    institucion = models.CharField(max_length=50)
    def __str__(self):
        return self.institucion

class Inscritos(models.Model): 
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    fechaInscripcion = models.DateField()
    institucion = models.ForeignKey(Institucion, on_delete= models.CASCADE)
    horaInscripcion = models.TimeField()
    estados = models.CharField(max_length=50, choices= elecciones)
    observacion = models.CharField(max_length=50, blank= True)

