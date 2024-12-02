from django.db import models
from django.conf import settings

class Producto(models.Model):
    """
    Modelo que representa un producto en el inventario.

    Esta clase almacena toda la información relacionada con los productos,
    incluyendo sus detalles básicos, categorización y relación con proveedores.

    Attributos
        nombre (str): Nombre del producto
        descripcion (str): Descripción detallada del producto
        precio (decimal): Precio del producto
        stock (int): Cantidad disponible en inventario
        sku (str): Código único del producto
        categoria (Categoria): Categoría a la que pertenece el producto
        proveedor (Proveedor): Proveedor del producto
        promocion (str): Información sobre promociones vigentes
    """
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    sku = models.CharField(max_length=50, unique=True, null=True, blank=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    proveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE, null=True, blank=True)
    promocion = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        """
        Retorna una representación en string del producto.

        Returns
            str: Nombre del producto
        """
        return self.nombre

class Categoria(models.Model):
    """
    Modelo que representa una categoría de productos.

    Esta clase permite organizar los productos en diferentes categorías
    para una mejor clasificación y organización del inventario.

    Attributos
        nombre (str): Nombre de la categoría
        descripcion (str): Descripción de la categoría
    """
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        """
        Retorna una representación en string de la categoría.

        Return
            str: Nombre de la categoría
        """
        return self.nombre

class Proveedor(models.Model):
    """
    Modelo que representa un proveedor de productos.

    Esta clase almacena la información de contacto y detalles
    de los proveedores que suministran productos al inventario.

    Attributos
        nombre (str): Nombre del proveedor
        info_contacto (str): Información de contacto del proveedor
        direccion (str): Dirección física del proveedor
    """
    nombre = models.CharField(max_length=100)
    info_contacto = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        """
        Retorna una representación en string del proveedor.

        Return
            str: Nombre del proveedor
        """
        return self.nombre

class RegistroInventario(models.Model):
    """
    Modelo que registra los movimientos del inventario.

    Esta clase mantiene un registro de todas las transacciones y cambios
    realizados en el inventario, incluyendo quién realizó el cambio y cuándo.

    Attributos
        usuario (User): Usuario que realizó el registro
        producto (Producto): Producto afectado
        cantidad (int): Cantidad modificada
        fecha (datetime): Fecha y hora del registro
    """
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='registros')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Retorna una representación en string del registro de inventario.

        Return
            str: Cadena con el formato "usuario - producto - fecha"
        """
        return f" {self.usuario.username} - {self.producto.nombre} - {self.fecha}"