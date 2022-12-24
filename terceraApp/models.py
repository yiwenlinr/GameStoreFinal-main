from django.db import models
from segundaApp.models import Empleados

TIPO = (
        ('Portatil','Portatil'),
        ('Fijo','Fijo'),
    )

class Consola(models.Model):
    modelo = models.CharField(max_length=50)
    tipo = models.CharField(max_length=8, null=True, choices=TIPO)
    marca = models.CharField(max_length=50)
    capacidad = models.CharField(max_length=50)
    peso = models.CharField(max_length=6)
    garantia = models.CharField(max_length=50)
    empleado = models.ForeignKey(Empleados, on_delete=models.CASCADE)

    def n_consola(self):
        return "{}".format(self.empleado)
    def __str__(self):
        return self.n_consola()