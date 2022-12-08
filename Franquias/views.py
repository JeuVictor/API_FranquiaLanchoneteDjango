from rest_framework import viewsets
from Franquias.models import franquia
from Franquias.serializer import FranquiasSerializer

class FranquiaViewSets (viewsets.ModelViewSet):
    queryset = franquia.objects.all()
    serializer_class = FranquiasSerializer
