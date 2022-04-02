from ast import List
from dataclasses import fields
from django import forms
from Stock.models import *

#Formulario para alta de nuevo producto/os (Hereda directamente de Stock por usamos forms.ModelForm y no forms.Form)

UNIDADES = [
    ('Kgs', 'Kilogramos'), 
    ('Grs', 'Gramos'), 
    ('Lts', 'Litros'),
    ('CCs', 'Centimetros Cubicos'),
    ('Uni', 'Unitario')
    ]

# ('', 'Selecciona una unidad de medida.'), VER COMO INCORPORAR EL VACIO COMO VALOR INICIAL y NO CAGARLA

class StockForm(forms.ModelForm):
        
    unidad = forms.CharField(widget=forms.Select(choices=UNIDADES))
        
    class Meta:
        model = Stock
        fields = ['rubro', 'subrubro', 'nombre', 'unidad']
        
        