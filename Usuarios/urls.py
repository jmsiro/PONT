from django.urls import path
from Usuarios import views

urlpatterns = [
    path('crear_usuario/', views.usuario_form, name="Crear Usuario" ),
]