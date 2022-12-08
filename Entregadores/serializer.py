from rest_framework import serializers
from Entregadores.models import entregador

class EntregadoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = entregador
        fields = ['id', 'Nome', 'CNH','Endereco','Veiculo','Placa']

