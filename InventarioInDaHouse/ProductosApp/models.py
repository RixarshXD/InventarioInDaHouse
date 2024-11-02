from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    precio = models.FloatField()
    descripcion = models.TextField(max_length=100)
    stock = models.IntegerField()
    promocion = models.CharField()
    
    # imagen = models.ImageField(upload_to='productos', null=True, blank=True)

    def __str__(self):
        return self.nombre