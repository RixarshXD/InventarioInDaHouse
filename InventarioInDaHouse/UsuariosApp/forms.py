from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class FormUsuario(UserCreationForm):
    class Meta:
        model = Usuario
        fields = [
            'username',
            'first_name',
            'last_name',
            'rut',
            'email',
            'role',
            'password1',
            'password2',
        ]
        
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de usuario'
            }),
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
                'placeholder': 'RUT'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Correo electrónico'
            }),
            'role': forms.Select(attrs={
                'class': 'form-control'
            }),
        }

class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario', widget=forms.TextInput)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)