from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    """
    Gestor personalizado para el modelo de Usuario.
    Extiende BaseUserManager para personalizar la creación de usuarios.
    """
    
    def create_user(self, email, password=None, **extra_fields):
        """
        Crea y guarda un Usuario con el email y contraseña dados.

        
            email (str): Email del usuario
            password (str, opcional): Contraseña del usuario. Por defecto None.
     
            Usuario: Nueva instancia de Usuario creada

      
            ValueError: Si no se proporciona un email
        """
        if not email:
            raise ValueError('El Email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Crea y guarda un SuperUsuario con el email y contraseña dados.

        
            email (str): Email del superusuario
            password (str, opcional): Contraseña del superusuario. Por defecto None.

        Returns:
            Usuario: Nueva instancia de SuperUsuario creada
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'Gerente')
        return self.create_user(email, password, **extra_fields)

class Usuario(AbstractUser):
    """
    Modelo personalizado de Usuario que extiende AbstractUser.
    
    Este modelo utiliza el email como identificador único en lugar del username
    y añade campos adicionales como rol y rut.

    
        email (EmailField): Campo único para identificar al usuario
        role (CharField): Rol del usuario en el sistema (Gerente/Vendedor/Encargado)
        rut (CharField): RUT chileno del usuario
        groups (ManyToManyField): Grupos a los que pertenece el usuario
        user_permissions (ManyToManyField): Permisos específicos del usuario
    """

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
        """
        Metaclase para definir atributos del modelo Usuario.
        """
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'
        
    def __str__(self):
        """
        Representación en string del Usuario.

        
            str: Email del usuario
        """
        return self.email
