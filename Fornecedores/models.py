from django.db import models

# Create your models here.
class fornecedor(models.Model):
    Nome = models.CharField(max_length=50)
    CNPJ = models.CharField(max_length=14)
    PRODUTO = models.CharField(max_length=50)
    QUANTIDADE = models.CharField(max_length=10)
    Contato = models.CharField(max_length=50)

    def _str_(self):
        return self.Nome