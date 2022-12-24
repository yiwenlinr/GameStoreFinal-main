from rest_framework.viewsets import ModelViewSet
from segundaApp.models import Empleados
from segundaApp.api.serializers import EmpleadosSerializer



class EmpleadosApiViewSet(ModelViewSet):
    serializer_class = EmpleadosSerializer
    queryset = Empleados.objects.all()