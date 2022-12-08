from rest_framework import serializers
from Clientes.models import clientes

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = clientes
        fields = ['id', 'Nome', 'CPF','Endereco','Cartao','Contato']
