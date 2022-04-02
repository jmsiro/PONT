from django import forms
from Compras.models import *

#Formulario para alta de nuevo producto/os (Hereda directamente de Stock por usamos forms.ModelForm y no forms.Form)

DOCUMENTO = [
    ('FC', 'Factura'), 
    ('NC', 'Nota de Credito'), 
    ('ND', 'Nota de Debito'),
    ('OT', 'Otro'),
    ]

TIPO = [
    ('A', 'A'), 
    ('B', 'B'), 
    ('C', 'C'),
    ('X', 'X'),
    ]

ALICUOTA = [
    ('10.5', '10,5%'), 
    ('21', '21%'), 
    ('27', '27%'),
    ('0', 'No Gravado'),
    ]

# Var como hacer con los campos calculados.
# Ver buscador de productos y que la unidad se cargue auntomaticamente
# Ver para poder cargar multiples productos (Formato tabla, encabezado y linea por linea cada producto)

class ComprasForm(forms.ModelForm):
        
    fecha = forms.DateTimeField()
    tipo_comprobante1 =forms.CharField(widget=forms.Select(choices=DOCUMENTO))
    tipo_comprobante2 =forms.CharField(widget=forms.Select(choices=TIPO))
    alicuota_iva = forms.CharField(widget=forms.Select(choices=ALICUOTA))
        
        
    class Meta:
        model = Compras
        fields = ['fecha', 'proveedor', 'cuit', 'tipo_comprobante1', 'tipo_comprobante2', 'numero_comprobante', 'producto', 'unidad', 'cantidad','precio_unitario', 'importe_neto', 'alicuota_iva', 'importe_iva', 'no_gravado', 'percepciones', 'importe_total']
    
