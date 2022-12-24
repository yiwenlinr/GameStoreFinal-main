from rest_framework.routers import DefaultRouter
from terceraApp.api.views import ConsolaApiViewSet

router_Consola = DefaultRouter()

router_Consola.register(prefix='Consola',basename='Consola',viewset=ConsolaApiViewSet)