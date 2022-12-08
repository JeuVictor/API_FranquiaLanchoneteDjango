from django.db import models

# Create your models here.

class clientes(models.Model):
    Nome = models.CharField(max_length=50)
    CPF = models.CharField(max_length=11)
    Endereco = models.CharField(max_length=100)
    Cartao = models.CharField(max_length=50)
    Contato = models.CharField(max_length=50)

    def _str_(self):
        return self.Nome
        
        

