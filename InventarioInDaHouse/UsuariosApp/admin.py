from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UsuarioAdmin(UserAdmin):
    # Campos que se mostrarán en la lista
    list_display = [
        'username',
        'first_name',
        'last_name', 
        'email',
        'role',
        'is_active'
    ]
    
    # Campos para búsqueda
    search_fields = [
        'username',
        'first_name',
        'last_name',
        'email'
    ]
    
    # Filtros disponibles
    list_filter = ['role', 'is_active']
    
    # Campos en el formulario de edición
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información Personal', {'fields': (
            'first_name',
            'last_name',
            'email',
            'role'
        )}),
        ('Permisos', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions'
        )}),
    )
    
    # Campos para crear nuevo usuario
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'email',
                'password1',
                'password2',
                'role',
                'is_staff',
                'is_active'
            ),
        }),
    )

admin.site.register(Usuario, UsuarioAdmin)