from .models import Usuario
from rest_framework import viewsets, permissions
from .serializers import UsuarioSerializers

class UsuarioViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar usuarios a través de la API REST.
    
    Proporciona endpoints para operaciones CRUD sobre usuarios:
    - Listar usuarios
    - Crear usuarios
    - Obtener detalles de usuario
    - Actualizar usuario 
    - Eliminar usuario
    """
    queryset = Usuario.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UsuarioSerializers