from django.db import models
from django.contrib.auth.models import User

class Pessoa(models.Model):
    nome=models.CharField(max_length=256)
    nasc=models.DateField(null=True)
    ativa=models.BooleanField(default=True)


    def __str__(self) -> str:
        return self.nome

class Contato(models.Model):
    nome=models.CharField(max_length=256)
    email=models.EmailField(max_length=256)
    telefone=models.CharField(max_length=20)
    pessoa=models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nome




# Create your models here.
