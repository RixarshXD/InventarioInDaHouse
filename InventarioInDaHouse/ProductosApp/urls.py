from django.urls import path
from .views import listado_productos, registrar_producto, actualizar_producto, eliminar_producto

urlpatterns = [
    path('', listado_productos, name='listado'),
    path('registrar/',registrar_producto , name='registrar/productos'),
    path('actualizar_producto/<int:id>/',actualizar_producto , name='actualizar_producto'),
    path('eliminar_producto/<int:id>/',eliminar_producto , name='eliminar_producto'),
]
