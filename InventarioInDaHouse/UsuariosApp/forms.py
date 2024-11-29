from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
import re

class FormUsuario(UserCreationForm):
    """
    Formulario para crear y actualizar usuarios.
    
    Validaciones:
    - RUT: Debe seguir el formato chileno XX.XXX.XXX-X
    - Contraseña: Mínimo 8 caracteres, debe incluir letra y número
    
    Campos personalizados:
    - first_name: Nombre del usuario
    - last_name: Apellido del usuario
    - rut: RUT chileno
    - email: Correo electrónico (usado como username)
    - role: Rol del usuario en el sistema
    - password1: Contraseña
    - password2: Confirmación de contraseña
    """
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña',
            'pattern': '^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$',
            'title': 'La contraseña debe tener al menos 8 caracteres, una letra y un número'
        })
    )
    
    password2 = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Repetir contraseña',
            'pattern': '^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$',
            'title': 'La contraseña debe tener al menos 8 caracteres, una letra y un número'
        })
    )

    def clean_rut(self):
        rut = self.cleaned_data['rut']
        if not re.match(r'^\d{2}\.\d{3}\.\d{3}-[\dkK]$', rut):
            raise forms.ValidationError('El RUT debe tener el formato XX.XXX.XXX-X')
        return rut

    class Meta:
        model = Usuario
        fields = [
            'first_name',
            'last_name',
            'rut',
            'email',
            'role',
            'password1',
            'password2',
        ]
        
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellido'
            }),
            'rut': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 12.345.678-9',
                'pattern': '^\d{2}\.\d{3}\.\d{3}-[\dkK]$',
                'title': 'Formato requerido: XX.XXX.XXX-X'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Correo electrónico'
            }),
            'role': forms.Select(attrs={
                'class': 'form-control'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Contraseña'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Repetir contraseña'
            }),
        }

class LoginForm(forms.Form):
    """
    Formulario para autenticación de usuarios.
    
    Campos:
    - email: Correo electrónico del usuario
    - password: Contraseña 
    """
    email = forms.EmailField(label='Correo electrónico', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))