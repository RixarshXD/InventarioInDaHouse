from django.urls import path
from .views import listado_productos, registrar_producto, actualizar_producto

urlpatterns = [
    path('', listado_productos, name='listado'),
    path('registrar/',registrar_producto , name='registrar/productos'),
    path('actualizar/<int:id>/',actualizar_producto , name='actualizar/productos'),
]
