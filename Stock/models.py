from pyexpat import model
from django.db import models

# Create your models here.

class Stock(models.Model):
    
    rubro = models.CharField(max_length=80) #Carnes, verduras, bebida, etc...
    subrubro =models.CharField(max_length=80) # Vacuna, cerdo, agua, vino, ect...
    nombre = models.CharField(max_length=80) #Nombre producto
    unidad = models.CharField(max_length=8) #Kilo, gramo, litro, etc...
    cantidad = models.CharField(max_length=8) #Unidades
    costo = models.CharField(max_length=8)  #Valor de adquisición de ultima compra (NETO DE IVA)
    ultima_compra = models.DateTimeField(auto_now=False, auto_now_add=False) #Fecha ultima compra