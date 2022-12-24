from rest_framework.routers import DefaultRouter
from segundaApp.api.views import EmpleadosApiViewSet

router_empleados = DefaultRouter()

router_empleados.register(prefix='empleados',basename='empleados',viewset=EmpleadosApiViewSet)