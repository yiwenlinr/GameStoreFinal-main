from django.contrib import admin
from primeraApp.models import Videojuegos

@admin.register(Videojuegos)
class VideojuegosAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','desarrollador','generos','plataformas','fecha_lanzamiento','puntuacion')
