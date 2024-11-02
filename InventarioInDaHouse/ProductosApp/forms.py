from django import forms
from .models import Producto

# se crean las opciones para el estado de la promoción del producto.
ESTADOS = [
    ('Sin estado','---Sin estado---'),
    ('activo','Activo'),
    ('inactivo','Inactivo')]

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
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(
                attrs={'class':'form-control'}),
            
            # se agrega el select para la categoría.
            'categoria': forms.Select(
                choices=CATEGORIA,
                attrs={'class':'form-control'}),
            
            'descripcion': forms.Textarea(
                attrs={'class':'form-control'}),
            
            'precio': forms.NumberInput(
                attrs={'class':'form-control'}),
            
            'stock': forms.NumberInput(
                attrs={'class':'form-control'}),
            
            # se agrega el select para el estado de la promoción.
            'promocion': forms.Select(
                choices=ESTADOS, 
                attrs={'class':'form-control'}),
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
        categoria = self.cleaned_data.get('categooria')
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

