from django.urls import path
from Compras import views

urlpatterns = [
    path('', views.compras, name="Compras" ),
    path('cargar_comprobante/', views.compras_form, name="Cargar comprobante" ),
]