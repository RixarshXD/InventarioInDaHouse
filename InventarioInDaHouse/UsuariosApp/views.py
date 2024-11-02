from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm

# Create your views here.

def listado_usuarios(request):
    usuarios = Usuario.objects.all()
    data = {'usuarios': usuarios}
    return render(request, 'UsuariosApp/ListadoUsuarios.html')

def registrar_usuario(request):
    form = UsuarioForm()
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return listado_usuarios(request)
    data = {'form': form}
    return listado_usuarios('Usuarios/RegistrarUsuarios.html',data)
    
def eliminar_usuario(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    return redirect('listado_usuarios')

def modificar_usuario(request, id):
    usuario = Usuario.objects.get(id=id)
    form = UsuarioForm(instance=usuario)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return listado_usuarios(request)
    data = {'form': form}
    return render(request, 'Usuarios/registrarUsuarios.html', data)