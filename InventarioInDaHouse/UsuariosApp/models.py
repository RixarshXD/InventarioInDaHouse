from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El Email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'Gerente')
        return self.create_user(email, password, **extra_fields)

class Usuario(AbstractUser):
    ROLES = [
        ('Gerente', 'Gerente'),
        ('Vendedor', 'Vendedor'),
        ('Encargado', 'Encargado'),
    ]
    
    username = None
    email = models.EmailField('email', unique=True)
    role = models.CharField(max_length=50, choices=ROLES, default='Vendedor')
    rut = models.CharField(max_length=12, unique=True, null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='custom_user_set',
        help_text='The groups this user belongs to.'
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_set',
        help_text='Specific permissions for this user.'
    )

    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'role']

    class Meta:
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'
        
    def __str__(self):
        return self.email
