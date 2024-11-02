from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

# Create your views here.

def ListadoProductos(request):
    productos = Producto.objects.all()
    data = {'productos': productos}
    return render(request, 'ProductosApp/ListadoProductos.html', data)

def RegistrarProducto(request):
    form = ProductoForm()
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return ListadoProductos(request)
    data = {'form':form}
    return render(request, 'ProductosApp/RegistrarProducto.html', data)

def EliminarProducto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('ListadoProductos')

def ActualizarProducto(request, id):
    producto = Producto.objects.get(id=id)
    form = ProductoForm(instance=producto)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return ListadoProductos(request)
    data = {'form': form}
    return render(request, 'ProductosApp/RegistrarProducto.html', data)
