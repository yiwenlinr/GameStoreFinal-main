from django.db import models
from segundaApp.models import Empleados

class Videojuegos(models.Model):
    nombre = models.CharField(max_length=50)
    desarrollador = models.CharField(max_length=50)
    generos = models.CharField(max_length=50)
    plataformas = models.CharField(max_length=50)
    fecha_lanzamiento = models.DateField()
    puntuacion = models.CharField(max_length=2)
    empleado = models.ForeignKey(Empleados, on_delete=models.CASCADE)

    def n_empleado(self):
        return "{}".format(self.empleado)
    def __str__(self):
        return self.n_empleado()