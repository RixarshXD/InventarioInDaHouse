from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class CustomUserAdmin(UserAdmin):
    model = Usuario
    list_display = ('email', 'first_name', 'last_name', 'role', 'rut', 'is_staff')
    ordering = ('email',)
    search_fields = ('email', 'first_name', 'last_name', 'rut')
    list_filter = ('role', 'is_staff', 'is_superuser')
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Información Personal', {'fields': ('first_name', 'last_name', 'rut', 'role')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'rut', 'role', 'is_staff', 'is_superuser')}
        ),
    )

admin.site.register(Usuario, CustomUserAdmin)