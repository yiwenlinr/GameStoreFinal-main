from django.db import models
from django.core import validators

class Empleados(models.Model):
    nombre = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    telefono = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    horario = models.CharField(max_length=50)
    
    def n_empleado(self):
        return "{}".format(self.nombre)
    def __str__(self):
        return self.n_empleado()