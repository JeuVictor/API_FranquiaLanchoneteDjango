from django.db import models

class entregador(models.Model):
    Nome = models.CharField(max_length=50)
    CNH = models.CharField(max_length=9)
    Endereco = models.CharField(max_length=100)
    Veiculo = models.CharField(max_length=20)
    Placa = models.CharField(max_length=7)

    def _str_(self):
        return self.Nome
# Create your models here.
