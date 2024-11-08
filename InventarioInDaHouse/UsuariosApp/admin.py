from django.contrib import admin
from .models import Usuario

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'rut', 'correo', 'contrasena','contrasena2', 'fecha_nacimiento', 'tipo_usuario']
    search_fields = ['nombre', 'rut', 'tipo_usuario']
    
admin.site.register(Usuario, UsuarioAdmin)