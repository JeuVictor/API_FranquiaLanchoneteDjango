from django.contrib import admin
from Fornecedores.models import fornecedor
# Register your models here.
class FORNECEDOR(admin.ModelAdmin):
    list_display = ('id', 'Nome', 'CNPJ','PRODUTO', 'QUANTIDADE', 'Contato')
    list_display_links = ('id', 'Nome', 'CNPJ')
    search_fields = ('Nome',)

admin.site.register(fornecedor, FORNECEDOR) 
# Register your models here.
