from rest_framework import serializers
from .models import Producto

class ProductoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at', ]
        