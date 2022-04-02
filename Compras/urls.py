from django.urls import path
from Compras import views

urlpatterns = [
    path('cargar_comprobante/', views.compras_form, name="Cargar COmprobante" ),
]