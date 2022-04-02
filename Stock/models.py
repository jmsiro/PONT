from pyexpat import model
from django.db import models

# Create your models here.

class Stock(models.Model):
    
    nombre = models.CharField(max_length=80)
    unidad = models.CharField(max_length=8)
    cantidad = models.CharField(max_length=8)
    costo = models.CharField(max_length=8)
    precio = models.CharField(max_length=8)
    ultima_compra = models.DateTimeField(auto_now=False, auto_now_add=False)