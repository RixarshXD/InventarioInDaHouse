from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
import re

class FormUsuario(UserCreationForm):
    """
    Formulario para la creación y actualización de usuarios en el sistema.

    Este formulario extiende de UserCreationForm y personaliza los campos
    y validaciones para el modelo Usuario.

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
        """
        Valida el formato del RUT chileno.
        """
        rut = self.cleaned_data['rut']
        if not re.match(r'^\d{2}\.\d{3}\.\d{3}-[\dkK]$', rut):
            raise forms.ValidationError('El RUT debe tener el formato XX.XXX.XXX-X')
        return rut

    class Meta:
        """
        Metaclase que define el modelo y los campos del formulario.SS
        """
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
    Formulario para la autenticación de usuarios en el sistema.

    Este formulario maneja el proceso de login de usuarios mediante
    correo electrónico y contraseña.

    """
    email = forms.EmailField(label='Correo electrónico', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))