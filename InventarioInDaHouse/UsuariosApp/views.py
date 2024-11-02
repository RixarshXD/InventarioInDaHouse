from django.shortcuts import render, redirect
from .models import Usuario
from .forms import FormUsuario

# Create your views here.

def listado_usuarios(request):
    usuarios = Usuario.objects.all()
    data = {'usuarios': usuarios}
    return render(request, 'UsuariosApp/ListadoUsuarios.html', data)

def registrar_usuario(request):
    form = FormUsuario()
    if request.method == 'POST':
        form = FormUsuario(request.POST)
        if form.is_valid():
            form.save()
            return listado_usuarios(request)
    data = {'form': form}
    return listado_usuarios('UsuariosApp/RegistrarUsuarios.html',data)
    
def eliminar_usuario(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    return redirect('listado_usuarios')

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