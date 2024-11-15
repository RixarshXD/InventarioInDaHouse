from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class FormUsuario(UserCreationForm):
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
                'placeholder': 'RUT'
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
    email = forms.EmailField(label='Correo electrónico', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))