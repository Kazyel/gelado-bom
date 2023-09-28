from django.db import models

# Create your models here.

class Sorvete(models.Model):
    sabor = models.CharField(max_length=20)
    preco = models.FloatField()
    estoque = models.IntegerField()


class Picole(models.Model):

    class Tipo(models.TextChoices):
        COBERTURA = 'Cobertura', ('Cobertura')
        NORMAL = 'Sem cobertura', ('Sem cobertura')

    sabor = models.CharField(max_length=20)
    preco = models.FloatField()
    tipo = models.CharField(max_length=13, choices= Tipo.choices, default=Tipo.NORMAL)
    estoque = models.IntegerField()


class Acai(models.Model):

    class Tamanho(models.TextChoices):
        UM = '1 Litro', ('1 Litro')
        DOIS = '2 Litros', ('2 Litros')
        CINCO = '5 Litros', ('5 Litros')
        DEZ = '10 Litros', ('10 Litros')

    preco = models.FloatField()
    estoque = models.IntegerField()
    tamanho = models.CharField(max_length=12, choices= Tamanho.choices, default=Tamanho.UM)
 