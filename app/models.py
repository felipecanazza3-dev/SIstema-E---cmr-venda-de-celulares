from django.db import models
from dataclasses import dataclass


class Celular(models.Model):
    nome=models.CharField(max_length=200)
    preco=models.FloatField()
    modelo=models.CharField(max_length=200)
    descricao=models.TextField(max_length=1000)
    marca=models.CharField(max_length=150)
    def __str__(self):
        return f"{self.nome} -{self.preco} -  {self.modelo} - {self.descricao} - {self.marca}"
