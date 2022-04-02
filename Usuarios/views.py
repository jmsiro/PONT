from django.shortcuts import render
from Usuarios.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.

#Crea usuario utilizando el modelo de Django
def usuario_form(request):
    contexto = {}
    
    if request.POST:
        formulario = UsuarioForm(request.POST)
    
        if formulario.is_valid():
            formulario.save()
            nombre_usuario = formulario.cleaned_data.get("username")
            clave = formulario.cleaned_data.get("password1")
            usuario = authenticate(username = nombre_usuario, password=clave)
            
            return render(request,"01_inicio.html", {"mensaje":f"Hola {usuario.get_username()}, creaste exitosamente tu usuario!"})
        else:
            contexto["usuario_formulario"] = formulario    
    else:
        formulario = UsuarioForm()
        contexto ["usuario_formulario"] = formulario

    return render(request, "01_crear_usuario.html", contexto)