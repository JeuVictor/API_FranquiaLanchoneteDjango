from django.db import models

class produto(models.Model):
    Nome = models.CharField(max_length=50)
    Tipo = models.CharField(max_length=50)
    Validade = models.CharField(max_length=8)
    Preco = models.CharField(max_length=10)
    Fabricacao = models.CharField(max_length=8)

    def _str_(self):
        return self.Nome
# Create your models here.
