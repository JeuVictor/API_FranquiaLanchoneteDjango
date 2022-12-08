from rest_framework import viewsets
from Entregadores.models import entregador
from Entregadores.serializer import EntregadoresSerializer

class EntregadorViewSets (viewsets.ModelViewSet):
    queryset = entregador.objects.all()
    serializer_class = EntregadoresSerializer
