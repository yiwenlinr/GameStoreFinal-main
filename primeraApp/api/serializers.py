from rest_framework.serializers import ModelSerializer
from primeraApp.models import Videojuegos

class VideojuegosSerializer(ModelSerializer):
    class Meta:
        model = Videojuegos
        fields = ['nombre','desarrollador','generos','plataformas','fecha_lanzamiento','puntuacion']