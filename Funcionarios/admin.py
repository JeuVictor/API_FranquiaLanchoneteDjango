from django.contrib import admin
from Funcionarios.models import funcionario
# Register your models here.
class FUNCIONARIO(admin.ModelAdmin):
    list_display = ('id', 'Nome', 'PIS','Cargo', 'Salario', 'Contato')
    list_display_links = ('id', 'Nome', 'PIS')
    search_fields = ('Nome',)

admin.site.register(funcionario, FUNCIONARIO) 

# Register your models here.
