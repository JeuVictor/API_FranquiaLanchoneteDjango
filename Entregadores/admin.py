from django.contrib import admin
from Entregadores.models import entregador
# Register your models here.
class ENTREGADOR(admin.ModelAdmin):
    list_display = ('id', 'Nome', 'CNH','Endereco', 'Veiculo', 'Placa')
    list_display_links = ('id', 'Nome', 'CNH')
    search_fields = ('Nome',)

admin.site.register(entregador, ENTREGADOR) 
# Register your models here.
