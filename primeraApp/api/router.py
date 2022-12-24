from rest_framework.routers import DefaultRouter
from primeraApp.api.views import VideojuegoApiViewSet

router_videojuegos = DefaultRouter()

router_videojuegos.register(prefix='videojuego',basename='videojuego',viewset=VideojuegoApiViewSet)