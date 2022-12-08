from django.db import models

class funcionario(models.Model):
    Nome = models.CharField(max_length=50)
    PIS = models.CharField(max_length=11)
    Cargo = models.CharField(max_length=50)
    Salario = models.CharField(max_length=10)
    Contato = models.CharField(max_length=50)

    def _str_(self):
        return self.Nome
# Create your models here.
