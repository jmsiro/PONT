from django.urls import path
from Usuarios import views

urlpatterns = [
    path('', views.usuarios, name="Usuarios" ),
    path('crear_usuario/', views.usuario_form, name="Crear usuario" ),
]