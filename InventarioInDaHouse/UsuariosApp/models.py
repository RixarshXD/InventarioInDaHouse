from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission, BaseUserManager

class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El Email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'Gerente')
        return self._create_user(email, password, **extra_fields)

class Usuario(AbstractUser):
    ROLES = [
        ('Gerente', 'Gerente'),
        ('Vendedor', 'Vendedor'),
        ('Encargado', 'Encargado'),
    ]
    
    username = None  # Deshabilitamos el campo username
    email = models.EmailField(unique=True)
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

    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'role']

    def save(self, *args, **kwargs):
        if not self.id and hasattr(self, '_password'):
            self.real_password = self._password
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
