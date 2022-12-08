from rest_framework import viewsets
from Clientes.models import clientes
from Clientes.serializer import ClienteSerializer

class ClienteViewSets (viewsets.ModelViewSet):
    queryset = clientes.objects.all()
    serializer_class = ClienteSerializer

# Create your views here.
