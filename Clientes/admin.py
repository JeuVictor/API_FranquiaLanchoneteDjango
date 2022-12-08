from django.contrib import admin
from Clientes.models import clientes
# Register your models here.
class CLIENTES(admin.ModelAdmin):
    list_display = ('id', 'Nome', 'CPF','Endereco', 'Cartao', 'Contato')
    list_display_links = ('id', 'Nome', 'CPF')
    search_fields = ('Nome',)

admin.site.register(clientes, CLIENTES)    