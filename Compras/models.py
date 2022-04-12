from django.db import models
from Stock.models import Stock

# Create your models here.

class Compras(models.Model):

    fecha = models.DateTimeField()
    proveedor = models.CharField(max_length=100) 
    cuit = models.CharField(max_length=11) # Tipear sin guión (despues ver formato)
    tipo_comprobante1 = models.CharField(max_length=4) # FC, NC, ND, OT, etc...
    tipo_comprobante2 = models.CharField(max_length=1) # A, B, C, X, etc...
    numero_comprobante = models.CharField(max_length=13) # Autocompletar con ceros por delante
    
    producto = models.ForeignKey(Stock, related_name='producto_compras', on_delete=models.CASCADE) #Debe tomar valor desde BD Stock
    unidad = models.ForeignKey(Stock,  related_name='unidad_compras', on_delete=models.CASCADE) #Debe tomar valor desde BD Stock
    
    cantidad =models.CharField(max_length=20) #Unidades compradas
    precio_unitario = models.CharField(max_length=20) #Precio por Unidad calculado según UNIDAD DE MEDIDA, si la unidad el Kilo no usar precio de la lata por ejemplo, colocar equivalente.
    importe_neto = models.CharField(max_length=20) #Importe calculado
    
    alicuota_iva = models.CharField(max_length=20) #Alicuota: 21%, 10,5%, 27% o 0%
    importe_iva = models.CharField(max_length=20) #Importe calculado
    
    no_gravado = models.CharField(max_length=20) #Importe sin IVA 
    percepciones = models.CharField(max_length=20) 
    
    importe_total = models.CharField(max_length=20) #Importe calculado
    importe_total_control = models.CharField(max_length=20) #Importe tipeado
    
    @property
    def neto(self):
        p = self.precio_unitario 
        q = self.cantidad
        neto = p * q
        return neto
    
    @property
    def iva(self):
        neto = self.importe_neto 
        alicuota = self.alicuota_iva
        iva = neto * alicuota
        return iva
    
    @property
    def total(self):
        neto = self.importe_neto
        iva = self.importe_iva
        no_g = self.no_gravado
        percep = self.percepciones
        total = neto + iva + no_g + percep
        return total
    
    def save(self, *args, **kwargs):
        self.importe_neto = self.neto
        self.importe_iva = self.iva
        self.importe_total = self.total
        super(Compras, self).save(*args, **kwargs)