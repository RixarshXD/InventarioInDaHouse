from django.urls import path
from .views import listado_usuarios, registrar_usuario, actualizar_usuario, eliminar_usuario

urlpatterns = [
    path('', listado_usuarios, name='listado'),
    path('registrar/', registrar_usuario, name='registrar/usuario'),
    path('actualizar_usuario/<int:id>/', actualizar_usuario, name='actualizar_usuario'),
    path('eliminar_usuario/<int:id>/', eliminar_usuario, name='eliminar_usuario'),
]