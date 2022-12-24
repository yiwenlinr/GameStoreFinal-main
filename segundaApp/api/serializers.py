from rest_framework.serializers import ModelSerializer
from segundaApp.models import Empleados

class EmpleadosSerializer(ModelSerializer):
    class Meta:
        model = Empleados
        fields = ['nombre','cargo','email','telefono','direccion','horario']