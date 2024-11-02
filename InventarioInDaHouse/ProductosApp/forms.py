from django import forms
from .models import Producto


ESTADOS = [
    ('Sin estado','---Sin estado---'),
    ('activo','Activo'),
    ('inactivo','Inactivo')]

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
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'categoria': forms.Select(choices=CATEGORIA,attrs={'class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control'}),
            'precio': forms.NumberInput(attrs={'class':'form-control'}),
            'stock': forms.NumberInput(attrs={'class':'form-control'}),
            'promocion': forms.Select(choices=ESTADOS, attrs={'class':'form-control'}),
        }
     
     
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre.isalpha():
            raise forms.ValidationError("Un nombre solo debe contener letras.")
        return nombre
    
    def clean_categoria(self):
        categoria = self.cleaned_data.get('categooria')
        if categoria == 'Sin categoría':
            raise forms.ValidationError('Por favor, Seleccione una categoría')
        return categoria

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio < 0:
            raise forms.ValidationError('El precio no puede ser negativo')
        return precio     

    def clean_promocion(self):
        promocion = self.cleaned_data.get('promocion')
        if promocion == 'Sin estado':
            raise forms.ValidationError('Por favor, Seleccione un estado')
        return promocion

