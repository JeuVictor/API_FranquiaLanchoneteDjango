from rest_framework import serializers
from Fornecedores.models import fornecedor

class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = fornecedor
        fields = ['id', 'Nome', 'CNPJ','PRODUTO','QUANTIDADE','Contato']
