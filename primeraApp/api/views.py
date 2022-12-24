from rest_framework.viewsets import ModelViewSet
from primeraApp.models import Videojuegos
from primeraApp.api.serializers import VideojuegosSerializer



class VideojuegoApiViewSet(ModelViewSet):
    serializer_class = VideojuegosSerializer
    queryset = Videojuegos.objects.all()
