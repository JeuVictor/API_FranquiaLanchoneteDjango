from django.contrib import admin
from Produtos.models import produto
# Register your models here.
class PRODUTO(admin.ModelAdmin):
    list_display = ('id', 'Nome', 'Tipo','Validade', 'Preco', 'Fabricacao')
    list_display_links = ('id', 'Nome', 'Preco')
    search_fields = ('Nome',)

admin.site.register(produto, PRODUTO) 
# Register your models here.
