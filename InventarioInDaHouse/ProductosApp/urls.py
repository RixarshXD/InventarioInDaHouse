from django.urls import path
from .views import listado_productos, registrar_producto

urlpatterns = [
    path('', listado_Productos, name='listado'),
    path('registrar/', registrar_producto, name='registrar'),
]
