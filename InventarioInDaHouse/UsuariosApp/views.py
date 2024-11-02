from django.shortcuts import render, redirect
from .models import Usuario
from .forms import FormUsuario

# Create your views here.

# Se crea la vista para el listado de usuarios.
#Se obtienen todos los usuarios de la base de datos y se envían al template 'ListadoUsuarios.html'. 
def listado_usuarios(request):
    usuarios = Usuario.objects.all()
    data = {'usuarios': usuarios}
    return render(request, 'UsuariosApp/ListadoUsuarios.html', data)

# Se crea la vista para registrar un usuario.
# Se crea un formulario vacío para registrar un usuario.
# Si el formulario es válido, se guarda el usuario en la base de datos y se redirige a la lista de usuarios.
def registrar_usuario(request):
    form = FormUsuario()
    if request.method == 'POST':
        form = FormUsuario(request.POST)
        if form.is_valid():
            form.save()
            return listado_usuarios(request)
    data = {'form': form}
    return listado_usuarios('UsuariosApp/RegistrarUsuarios.html',data)
    
# Se crea la vista para eliminar un usuario.
# Se obtiene el usuario a eliminar y se elimina de la base de datos.
# Se redirige a la lista de usuarios.
def eliminar_usuario(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    return redirect('listado_usuarios')

# Se crea la vista para actualizar un usuario.
# Se obtiene el usuario a actualizar y se crea un formulario con los datos del usuario.
# Si el formulario es válido, se actualiza el usuario y se redirige a la lista de usuarios.
def modificar_usuario(request, id):
    usuario = Usuario.objects.get(id=id)
    form = FormUsuario(instance=usuario)
    if request.method == 'POST':
        form = FormUsuario(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return listado_usuarios(request)
    data = {'form': form}
    return render(request, 'UsuariosApp/registrarUsuarios.html', data)