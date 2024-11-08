from django import forms
from .models import Usuario

#Se crean las opciones para el tipo de usuario.
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
                       'placeholder': 'Apellido del Trabajador'}),
            
            'rut': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Rut del Trabajador'}),
            
            'correo': forms.EmailInput(
                attrs={'class': 'form-control',
                          'placeholder': 'Correo del Trabajador'}),
            
            'contrasena': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Contraseña del Trabajador'}),
            'contrasena2': forms.TextInput(
                attrs={'class': 'form-control',
                          'placeholder': 'Repetir Contraseña del Trabajador'}),
            
            'fecha_nacimiento': forms.DateInput(
                attrs={'class': 'form-control',
                       'type': 'date',
                       'placeholder': 'Fecha de nacimiento'}),
            # Se agrega el select para el tipo de usuario.
            'tipo_usuario': forms.Select(
                choices=tipo,
                attrs={'class': 'form-control',
                       'placeholder': 'Tipo de Trabajador'}),
        }
        
    
    # Se crean validaciones para algunos campos:
    
    # Validación para el 'nombre'. Solo se permiten letras.
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre.isalpha():
            raise forms.ValidationError("Un nombre solo debe contener letras.")
        return nombre

    # Validación para el 'apellido'. Solo se permiten letras.
    def clean_apellido(self):
        apellido = self.cleaned_data.get('apellido')
        if not apellido.isalpha():
            raise forms.ValidationError("Un apellido solo debe contener letras.")
        return apellido    
    
    # Validación para el 'rut'. El rut debe contener guión y no puntos.
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
    
    # Validación para el 'tipo'. La validación convierte la especificación del tipo en un campo obligatorio.
    def clean_tipo(self):
        tipo = self.cleaned_data.get('tipo')
        if tipo == 'Sin tipo':
            raise forms.ValidationError("Por favor, selecciona un tipo.")
        return tipo
    

    
