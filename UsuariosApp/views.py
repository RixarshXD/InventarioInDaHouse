from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, permission_required
from .models import Usuario
from .forms import FormUsuario, LoginForm
from django.core.exceptions import PermissionDenied
from django.contrib import messages

def loginUsuario(request):
    """
    Autentica al usuario en el sistema usando email y contraseña.
    
    
        request: Objeto request que contiene los datos del formulario de login.
    
    
        Renderiza la página de login o redirige a la página siguiente si la autenticación es exitosa.
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            try:
                # Intentar obtener el usuario por email
                user = Usuario.objects.get(email=email)
                # Autenticar usando el email como username
                auth_user = authenticate(request, username=email, password=password)
                if auth_user is not None:
                    login(request, auth_user)
                    messages.success(request, f'Bienvenido {auth_user.first_name}!')
                    next_url = request.GET.get('next', '/')
                    return redirect(next_url)
                else:
                    messages.error(request, 'Contraseña incorrecta')
            except Usuario.DoesNotExist:
                messages.error(request, 'No existe un usuario con ese email')
    else:
        form = LoginForm()
    return render(request, 'UsuariosApp/Login.html', {'form': form})


def logoutUsuario(request):
    """
    Cierra la sesión actual del usuario.
    

        request: Objeto request de la sesión actual.
    
  
        Redirige a la página principal después de cerrar sesión.
    """
    logout(request)
    return redirect('/')

@login_required
def listado_usuarios(request):
    """
    Muestra la lista de usuarios registrados en el sistema.
    Restringido a usuarios con roles Gerente o Encargado.
    
    
        request: Objeto request que contiene la información del usuario actual.
    
    
        Renderiza la página con el listado de usuarios incluyendo:
        - Lista completa de usuarios
        - Indicador si se muestran contraseñas (solo Gerente)
        - Información de permisos del usuario actual
    """
    try:
        usuario_actual = Usuario.objects.get(email=request.user.email)
        # Permitir acceso a Gerentes y Encargados
        if usuario_actual.role not in ['Gerente', 'Encargado']:
            messages.error(request, 'No tienes permisos para ver el listado de usuarios')
            return redirect('/')
        
        usuarios = Usuario.objects.all()
        # Solo Gerente puede ver contraseñas
        show_passwords = usuario_actual.role == 'Gerente'
            
        data = {
            'usuarios': usuarios,
            'show_passwords': show_passwords,
            'is_admin': usuario_actual.role == 'Gerente',
            'user_role': usuario_actual.role,
            'user_name': request.user.first_name
        }
        return render(request, 'UsuariosApp/ListadoUsuarios.html', data)
    except PermissionDenied:
        messages.warning(request, 'No tienes permisos para acceder a esta página.')
        return redirect('/')


@login_required
def registrar_usuario(request):
    """
    Gestiona el registro de nuevos usuarios en el sistema.
    Restringido a usuarios con rol Gerente.
    
    
        request: Objeto request con los datos del formulario de registro.
    
    
        Renderiza el formulario de registro o redirige al listado tras un registro exitoso.
    
    Note:
        Valida que las contraseñas coincidan y maneja errores en el proceso de registro.
    """
    try:
        usuario_actual = Usuario.objects.get(email=request.user.email)
        # Solo Gerente puede registrar usuarios
        if usuario_actual.role != 'Gerente':
            messages.error(request, 'Solo los gerentes pueden registrar usuarios')
            return redirect('listado')
            
        if request.method == 'POST':
            form = FormUsuario(request.POST)
            if form.is_valid():
                try:
                    if form.cleaned_data['password1'] != form.cleaned_data['password2']:
                        messages.error(request, 'Las contraseñas no coinciden')
                        return render(request, 'UsuariosApp/RegistrarUsuario.html', {'form': form})

                    usuario = Usuario.objects.create_user(
                        email=form.cleaned_data['email'],
                        password=form.cleaned_data['password1'],
                        first_name=form.cleaned_data['first_name'],
                        last_name=form.cleaned_data['last_name'],
                        role=form.cleaned_data['role'],
                        rut=form.cleaned_data['rut']
                    )
                    messages.success(request, 'Usuario registrado correctamente')
                    return redirect('listado')
                except Exception as e:
                    messages.error(request, f'Error al registrar: {str(e)}')
        else:
            form = FormUsuario()
        
        return render(request, 'UsuariosApp/RegistrarUsuario.html', {'form': form})
    except Usuario.DoesNotExist:
        messages.error(request, 'Usuario no encontrado')
        return redirect('listado')

    
@login_required
def eliminar_usuario(request, id):
    """
    Elimina un usuario del sistema.
    Restringido a usuarios con rol Gerente.
    
    
        request: Objeto request que contiene la información de la petición.
        id: Identificador único del usuario a eliminar.
    
    
        Redirige al listado de usuarios tras la eliminación.
    
    Note:
        Impide que un usuario se elimine a sí mismo.
    """
    if request.method == 'POST':
        try:
            usuario_actual = Usuario.objects.get(email=request.user.email)
            # Solo Gerente puede eliminar usuarios
            if usuario_actual.role != 'Gerente':
                messages.error(request, 'Solo los gerentes pueden eliminar usuarios')
                return redirect('listado')

            # Obtener usuario
            usuario = Usuario.objects.get(id=id)
            
            if usuario == request.user:
                messages.error(request, 'No puedes eliminarte a ti mismo')
                return redirect('listado')

            # Eliminar el usuario directamente
            usuario.delete()
            messages.success(request, 'Usuario eliminado correctamente')
            
        except Usuario.DoesNotExist:
            messages.error(request, 'Usuario no encontrado')
        except Exception as e:
            messages.error(request, f'Error al eliminar usuario: {str(e)}')
    return redirect('listado')

@login_required 
def actualizar_usuario(request, id):
    """
    Modifica los datos de un usuario existente.
    Restringido a usuarios con rol Gerente.
    
    
        request: Objeto request con los datos del formulario de actualización.
        id: Identificador único del usuario a actualizar.
    
    
        Renderiza el formulario de actualización o redirige al listado tras actualizar.
    
    Note:
        Usa el mismo template que el registro pero en modo actualización.
    """
    try:
        usuario_actual = Usuario.objects.get(email=request.user.email)
        # Solo Gerente puede actualizar usuarios
        if usuario_actual.role != 'Gerente':
            messages.error(request, 'Solo los gerentes pueden actualizar usuarios')
            return redirect('listado')
            
        usuario = Usuario.objects.get(id=id)
        form = FormUsuario(instance=usuario)
        if request.method == 'POST':        
            form = FormUsuario(request.POST, instance=usuario)
            if form.is_valid():
                form.save()
                return listado_usuarios(request)
        data = {'form': form}
        return render(request,'UsuariosApp/RegistrarUsuario.html', data)
    except Usuario.DoesNotExist:
        messages.error(request, 'Usuario no encontrado')
        return redirect('listado')
