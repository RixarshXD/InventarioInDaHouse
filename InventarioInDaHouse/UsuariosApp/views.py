from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Usuario
from .forms import FormUsuario
from django.http import HttpResponse


def listado_usuarios(request):
    """
    Se crea la vista para el listado de usuarios,
    Se obtienen todos los usuarios de la base de datos y se envían al template 'ListadoUsuarios.html'.
    """
    usuarios = Usuario.objects.all()
    data = {'usuarios': usuarios}
    return render(request, 'UsuariosApp/ListadoUsuarios.html', data)



def registrar_usuario(request):  
    """
    # Se crea la vista para registrar un usuario.
    # Se crea un formulario vacío para registrar un usuario.
    # Si el formulario es válido, se guarda el usuario en la base de datos y se redirige a la lista de usuarios.
    """
    form = FormUsuario()
    # if request.method == 'POST':
    #     form = FormUsuario(request.POST)
    #     if form.is_valid():
    #         #depurar
    #         print(request.POST)
    #         form.save()
    #         return listado_usuarios(request)
    # data = {'form': form}
    # return render(request, 'UsuariosApp/RegistrarUsuario.html',data)
    
    if request.method == 'GET':
        return render(request, 'UsuariosApp/RegistrarUsuario.html', {'form': form})
    else:
        try: 
            form = FormUsuario(request.POST)
            if request.POST['contrasena'] == request.POST['contrasena2']:
                if form.is_valid():
                    user = User.objects.create_user(username=request.POST['nombre'], password=request.POST['contrasena'])
                    user.save()
                    form.save()
                return render(request, 'UsuariosApp/RegistrarUsuario.html', {'form': form, 'error': 'Usuario registrado correctamente'})
        except:
            return render(request, 'UsuariosApp/RegistrarUsuario.html', {'form': form, 'error': 'El usuario ya existe'})

    return render(request, 'UsuariosApp/RegistrarUsuario.html', {'form': form, 'error': 'Las contraseñas no coinciden'})


    

def eliminar_usuario(request, id):
    """
    Se crea la vista para eliminar un usuario.
    Se obtiene el usuario a eliminar y se elimina de la base de datos.
    Se redirige a la lista de usuarios.
    """
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    return redirect(listado_usuarios)

def actualizar_usuario(request, id):
    """
    Se crea la vista para actualizar un usuario.
    Se obtiene el usuario a actualizar y se crea un formulario con los datos del usuario.
    Si el formulario es válido, se actualiza el usuario y se redirige a la lista de usuarios.
    """
    usuario = Usuario.objects.get(id=id)
    form = FormUsuario(instance=usuario)
    if request.method == 'POST':
        form = FormUsuario(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return listado_usuarios(request)
    data = {'form': form}
    return render(request,'UsuariosApp/RegistrarUsuario.html', data)