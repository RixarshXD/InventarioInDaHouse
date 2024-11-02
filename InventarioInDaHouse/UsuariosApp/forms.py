from django import forms
from .models import Usuario

tipo = [
    ('Sin tipo','---Selecciona un tipo--'),
    ('Vendedor','Vendedor'),
    ('Gerente', 'Gerente'),
    ('Encargado', 'Encargado'),]

class FormUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ("__all__")
        
        widgets = {
            'nombre': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Nombre '}),
            
            'apellido': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Apellido del usuario'}),
            
            'rut': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Rut del usuario'}),
            
            'correo': forms.EmailInput(
                attrs={'class': 'form-control',
                          'placeholder': 'Correo del usuario'}),
            
            'contrasena': forms.EmailInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Contraseña del doctor'}),
            
            'telefono': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Telefono del usuario'}),
            
            'fechaNacimiento': forms.DateInput(
                attrs={'class': 'form-control',
                       'type': 'date',
                       'placeholder': 'Fecha de nacimiento'}),
            
            'tipo_usuario': forms.Select(
                choices=tipo,
                attrs={'class': 'form-control',
                       'placeholder': 'Tipo de usuario'}),

        }
        
        
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre.isalpha():
            raise forms.ValidationError("Un nombre solo debe contener letras.")
        return nombre

    def clean_apellido(self):
        apellido = self.cleaned_data.get('apellido')
        if not apellido.isalpha():
            raise forms.ValidationError("Un apellido solo debe contener letras.")
        return apellido    
    
    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        if "-" not in rut:
            raise forms.ValidationError("El RUT debe contener el guión.")
        if "." in rut:
            raise forms.ValidationError("Ingrese su RUT sin puntos.")

        numerico, codigo_verificador = rut.split("-")

        if len(numerico) < 7 or len(numerico) > 8:
            raise forms.ValidationError("La longitud de la parte numérica no es válida.")
        if not numerico.isdigit():
            raise forms.ValidationError("La parte numérica debe ser un número.")
        if len(codigo_verificador) != 1 or (not codigo_verificador.isdigit() and codigo_verificador.lower() != "k"):
            raise forms.ValidationError("El código verificador debe ser un número o 'K'.")
        return rut
    
    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if len(telefono) < 9 or len(telefono) > 12:
            raise forms.ValidationError("El número de teléfono no es válido.")
        if not telefono.isdigit():
            raise forms.ValidationError("El número de teléfono debe ser un número.")
        return telefono
    
    def clean_tipo(self):
        tipo = self.cleaned_data.get('tipo')
        if tipo == 'Sin tipo':
            raise forms.ValidationError("Por favor, selecciona un tipo.")
        return tipo
    

    
