from django.urls import path
from .views import listado_usuarios, registrar_usuario, modificar_usuario, eliminar_usuario

urlpatterns = [
    path('', listado_usuarios, name='listado'),
    path('registrar/', registrar_usuario, name='registrar'),
    path('modificar/<int:id>/', modificar_usuario, name='modificar'),
    path('eliminar/<int:id>/', eliminar_usuario, name='eliminar'),
]