from rest_framework.serializers import ModelSerializer
from terceraApp.models import Consola

class ConsolaSerializer(ModelSerializer):
    class Meta:
        model = Consola
        fields = ['modelo','tipo','marca','capacidad','peso','garantia']