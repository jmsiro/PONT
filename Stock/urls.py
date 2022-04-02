from django.urls import path
from Stock import views

urlpatterns = [
    path('crear_producto/', views.stock_form, name="Crear producto" ),
]