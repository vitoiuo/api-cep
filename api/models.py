from dataclasses import field
from enum import unique
from django.db import models


class Estado(models.Model):
    nome = models.CharField(max_length=128, unique=True)
    sigla = models.CharField(max_length=8, unique=True)

class Cidade(models.Model):
    nome = models.CharField(max_length=128, unique=True)
    estado_id = models.ForeignKey(Estado, on_delete=models.PROTECT)

class Cep(models.Model):
    cep = models.CharField(max_length=8, unique=True)
    logradouro = models.CharField(max_length=256)
    bairro = models.CharField(max_length=256)
    cidade_id = models.ForeignKey(Cidade, on_delete=models.PROTECT)
    estado_id = models.ForeignKey(Estado, on_delete=models.PROTECT)

    class Meta:
        unique_together = [['cidade_id', 'estado_id']]
        

# Create your models here.
