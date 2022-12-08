
from django.contrib import admin
from django.urls import path, include
from Clientes.views import ClienteViewSets
from Entregadores.views import EntregadorViewSets
from Fornecedores.views import FornecedorViewSets
from Franquias.views import FranquiaViewSets
from Funcionarios.views import FuncionarioViewSets
from Produtos.views import ProdutosViewSets
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cliente', ClienteViewSets)
router.register(r'entregador', EntregadorViewSets)
router.register(r'fornecedor', FornecedorViewSets)
router.register(r'franquia', FranquiaViewSets)
router.register(r'funcionario', FuncionarioViewSets)
router.register(r'produtos', ProdutosViewSets)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
