from django.urls import path
from .views import ListadoProductos, RegistrarProducto

urlpatterns = [
    path('', ListadoProductos, name='listado'),
    path('registrar/', RegistrarProducto, name='registrar'),
]
