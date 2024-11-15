from django.urls import path
from . import views

urlpatterns = [
    path('', views.listado_productos, name='listado_productos'),
    path('productos/nuevo/', views.registrar_producto, name='registrar_producto'),
    path('productos/editar/<int:pk>/', views.actualizar_producto, name='editar_producto'),
    path('productos/detalle/<int:pk>/', views.detalle_producto, name='detalle_producto'),
    path('productos/eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
]
