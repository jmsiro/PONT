from django.shortcuts import render
from Stock.forms import *

# Create your views here.

def stock(request):

    return render(request, "00_stock.html")

def stock_form(request):
    contexto = {}
    
    if request.POST:
        formulario = StockForm(request.POST)

        if formulario.is_valid():
            
            #REVISAR Manejo de errores en carga manual y por BD
            #unidad = formulario.cleaned_data.get("unidad")
            # if unidad == '':
                
            formulario.save()
            
            return render(request,"01_inicio.html", {"mensaje":f"Creaste exitosamente el/los producto/os!"})
        else:
            contexto["stock_formulario"] = formulario    
    else:
        formulario = StockForm()
        contexto ["stock_formulario"] = formulario

    return render(request, "01_crear_producto.html", contexto)