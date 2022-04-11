from django.urls import path
from Stock import views

urlpatterns = [
    path('', views.stock, name="Stock" ),
    path('crear_producto/', views.stock_form, name="Crear producto" ),
]