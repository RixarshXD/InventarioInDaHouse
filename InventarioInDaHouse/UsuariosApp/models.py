from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth.hashers import make_password

class Usuario(AbstractUser):
    ROLES = [
        ('Gerente', 'Gerente'),
        ('Vendedor', 'Vendedor'),
        ('Encargado', 'Encargado'),
    ]
    
    # Campos personalizados
    role = models.CharField(max_length=50, choices=ROLES, default='Vendedor')
    rut = models.CharField(max_length=10, unique=True, null=True, blank=True)  
    real_password = models.CharField(max_length=128, null=True, blank=True)  # Nuevo campo
    
    # Redefinir relaciones para evitar conflictos
    groups = models.ManyToManyField(
        Group,
        related_name='usuario_set',
        blank=True,
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='usuario_permissions_set',
        blank=True,
        verbose_name='user permissions',
    )

    def save(self, *args, **kwargs):
        if not self.id and self._password is not None:  # Solo al crear usuario nuevo
            self.real_password = self._password
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
