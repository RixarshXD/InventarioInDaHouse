from django import forms
from .models import Producto, Categoria, Proveedor, RegistroInventario

# se crean las opciones para el estado de la promoción del producto.
ESTADOS = [
    ('Sin estado','---Sin estado---'),
    ('activa','Activa'),
    ('inactiva','Inactiva')]

# se crean las opciones para la categoría del producto.
CATEGORIA = [
    ('Sin categoría','---Sin categoría---'),
    ('Polera','Polera'),
    ('Poleron','Poleron'),
    ('Pantalon','Pantalon'),
    ('Short','Short'),
    ('Zapatilla','Zapatilla'),
    ('Accesorio','Accesorio'),
]


class ProductoForm(forms.ModelForm):
    """
    Formulario para crear y actualizar productos.
    
    Validaciones:
    - Nombre: Solo permite letras
    - Categoría: No permite la opción 'Sin categoría'
    - Precio: No permite valores negativos
    - Promoción: Requiere seleccionar un estado válido
    """
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'sku', 'categoria', 'proveedor', 'promocion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'sku': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'proveedor': forms.Select(attrs={'class': 'form-control'}),
            'promocion': forms.TextInput(attrs={'class': 'form-control'}),
        }
     
    # Se crean validaaciones para algunos campos:
    
    # Validación para el 'nombre'. Solo se permiten letras.
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre.isalpha():
            raise forms.ValidationError("Un nombre solo debe contener letras.")
        return nombre
    
    # Validación para la 'categoria'. La validación convierte la especificación de la categoría en un campo obligatorio.
    def clean_categoria(self):
        categoria = self.cleaned_data.get('categoria')
        if categoria == 'Sin categoría':
            raise forms.ValidationError('Por favor, Seleccione una categoría')
        return categoria

    # Validación para el 'precio'. El precio no puede ser negativo.
    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio < 0:
            raise forms.ValidationError('El precio no puede ser negativo')
        return precio     

    # Validación para el estado de la promoción. La validación convierte la especificación del estado de la promoción en un campo obligatorio.
    def clean_promocion(self):
        promocion = self.cleaned_data.get('promocion')
        if promocion == 'Sin estado':
            raise forms.ValidationError('Por favor, Seleccione un estado')
        return promocion

class CategoriaForm(forms.ModelForm):
    """
    Formulario para crear y actualizar categorías de productos.
    
    Validaciones:
    - Nombre: Solo permite letras y espacios
    """
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre.replace(' ', '').isalpha():
            raise forms.ValidationError("El nombre solo debe contener letras")
        return nombre

class ProveedorForm(forms.ModelForm):
    """
    Formulario para crear y actualizar proveedores.
    
    Campos:
    - nombre: Nombre del proveedor
    - info_contacto: Información de contacto
    - direccion: Dirección física del proveedor
    """
    class Meta:
        model = Proveedor
        fields = ['nombre', 'info_contacto', 'direccion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'info_contacto': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
        }

class RegistroInventarioForm(forms.ModelForm):
    """
    Formulario para registrar movimientos de inventario.
    
    Campos:
    - producto: Producto afectado
    - cantidad: Cantidad a agregar/remover del inventario
    """
    class Meta:
        model = RegistroInventario
        fields = ['producto', 'cantidad']
