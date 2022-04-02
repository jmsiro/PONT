from django.shortcuts import render
from Compras.forms import *

# Create your views here.

def compras_form(request):
    contexto = {}
    
    if request.POST:
        formulario = ComprasForm(request.POST)

        if formulario.is_valid():
                
            formulario.save()
            
            return render(request,"01_inicio.html", {"mensaje":f"Cargaste exitosamente el comprobante!"})
        else:
            contexto["compras_formulario"] = formulario    
    else:
        formulario = ComprasForm()
        contexto ["compras_formulario"] = formulario

    return render(request, "01_cargar_comprobante.html", contexto)