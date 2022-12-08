from django.db import models

class franquia(models.Model):
    NomeProprietario = models.CharField(max_length=50)
    CNPJ = models.CharField(max_length=14)
    Endereco = models.CharField(max_length=100)
    Telefone = models.CharField(max_length=11)
    Email = models.CharField(max_length=50)

    def _str_(self):
        return self.NomeProprietario
# Create your models here.
