from django import forms
from .models import Producto


ESTADOS = [('activo','Activo'),('inactivo','Inactivo')]


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control'}),
            'precio': forms.NumberInput(attrs={'class':'form-control'}),
            'stock': forms.NumberInput(attrs={'class':'form-control'}),
            'promocion': forms.Select(choices=ESTADOS, attrs={'class':'form-control'}),
        }
        
        