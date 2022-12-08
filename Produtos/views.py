from rest_framework import viewsets
from Produtos.models import produto
from Produtos.serializer import Produtoserializer

class ProdutosViewSets (viewsets.ModelViewSet):
    queryset = produto.objects.all()
    serializer_class = Produtoserializer
