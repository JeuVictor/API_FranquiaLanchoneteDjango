from django.contrib import admin
from Franquias.models import franquia
# Register your models here.
class FRANQUIA(admin.ModelAdmin):
    list_display = ('id', 'NomeProprietario', 'CNPJ','Endereco', 'Telefone', 'Email')
    list_display_links = ('id', 'NomeProprietario', 'CNPJ')
    search_fields = ('NomeProprietario',)

admin.site.register(franquia, FRANQUIA) 
# Register your models here.
# Register your models here.
