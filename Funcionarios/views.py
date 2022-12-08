from rest_framework import viewsets
from Funcionarios.models import funcionario
from Funcionarios.serializer import FuncionarioSerializer

class FuncionarioViewSets (viewsets.ModelViewSet):
    queryset = funcionario.objects.all()
    serializer_class = FuncionarioSerializer
