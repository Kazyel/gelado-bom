from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Sorvete(models.Model):
    id = models.AutoField(primary_key=True);
    sabor = models.CharField(max_length=20)
    preco = models.FloatField()
    estoque = models.IntegerField()

    def __str__(self):
        return self.sabor

class Picole(models.Model):

    class Tipo(models.TextChoices):
        COBERTURA = 'Cobertura', ('Cobertura')
        NORMAL = 'Sem cobertura', ('Sem cobertura')

    id = models.AutoField(primary_key=True);
    sabor = models.CharField(max_length=20)
    preco = models.FloatField()
    tipo = models.CharField(max_length=13, choices= Tipo.choices, default=Tipo.NORMAL)
    estoque = models.IntegerField()

    def __str__(self):
        return self.sabor   


class Acai(models.Model):

    class Tamanho(models.TextChoices):
        UM = '1 Litro', ('1 Litro')
        DOIS = '2 Litros', ('2 Litros')
        CINCO = '5 Litros', ('5 Litros')
        DEZ = '10 Litros', ('10 Litros')
        
    id = models.AutoField(primary_key=True);
    preco = models.FloatField()
    estoque = models.IntegerField()
    tamanho = models.CharField(max_length=12, choices= Tamanho.choices, default=Tamanho.UM)

    def __str__(self):
        return self.tamanho
    
class ShopCartPicole(models.Model):
    produto = models.ForeignKey(Picole, null=True, on_delete=models.SET_NULL)
    quantidade = models.IntegerField(default=0, null=True, blank=True)
    
class ShopCartSorvete(models.Model):
     produto = models.ForeignKey(Sorvete, null=True, on_delete=models.SET_NULL)
     quantidade = models.IntegerField(default=0, null=True, blank=True)
     
class ShopCartAcai(models.Model):
     produto = models.ForeignKey(Acai, null=True, on_delete=models.SET_NULL)
     quantidade = models.IntegerField(default=0, null=True, blank=True)