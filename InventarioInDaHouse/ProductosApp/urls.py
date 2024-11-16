from django.urls import path
from . import views

urlpatterns = [
    path('', views.listado_productos, name='listado_productos'),
    path('productos/nuevo/', views.registrar_producto, name='registrar_producto'),
    path('productos/actualizar/<int:id>/', views.actualizar_producto, name='actualizar_producto'),  # Cambiado de editar a actualizar
    path('productos/detalle/<int:pk>/', views.detalle_producto, name='detalle_producto'),
    path('productos/eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
    path('categoria/nueva/', views.registrar_categoria, name='registrar_categoria'),
    path('proveedor/nuevo/', views.registrar_proveedor, name='registrar_proveedor'),
    path('registros/', views.lista_registros, name='lista_registros'),
    path('registros/nuevo/', views.agregar_registro, name='agregar_registro'),
]
