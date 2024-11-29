from .models import Producto
from rest_framework import viewsets, permissions
from .serializers import ProductoSerializers

class ProductoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar productos a través de la API REST.
    
    Attributes:
        queryset: QuerySet con todos los productos
        permission_classes: Permisos requeridos
        serializer_class: Clase serializadora
        
    Methods:
        list(): Retorna lista de productos
        create(): Crea nuevo producto
        retrieve(): Obtiene detalles de producto
        update(): Actualiza producto existente
        destroy(): Elimina producto
    """
    queryset = Producto.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProductoSerializers