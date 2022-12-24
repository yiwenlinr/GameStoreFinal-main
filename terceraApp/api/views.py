from rest_framework.viewsets import ModelViewSet
from terceraApp.models import Consola
from terceraApp.api.serializers import ConsolaSerializer



class ConsolaApiViewSet(ModelViewSet):
    serializer_class = ConsolaSerializer
    queryset = Consola.objects.all()