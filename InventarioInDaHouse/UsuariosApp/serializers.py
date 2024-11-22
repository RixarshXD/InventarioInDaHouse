from rest_framework import serializers
from .models import Usuario

class UsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        read_only_fields = ['id', 'last_login', 'date_joined', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', ]