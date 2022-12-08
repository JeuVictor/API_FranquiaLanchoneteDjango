from rest_framework import serializers
from Franquias.models import franquia

class FranquiasSerializer(serializers.ModelSerializer):
    class Meta:
        model = franquia
        fields = ['id', 'NomeProprietario', 'CNPJ','Endereco','Telefone','Email']