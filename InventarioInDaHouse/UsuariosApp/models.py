from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut = models.CharField(max_length=10)
    correo = models.EmailField(max_length=50)
    contrasena = models.CharField(max_length=50)
    telefono = models.CharField(max_length=12)
    fecha_nacimiento = models.DateField()
    tipo_usuario = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
