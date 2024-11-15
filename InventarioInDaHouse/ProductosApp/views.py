from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Producto
from .forms import ProductoForm


# Función para la página de inicio.
def index(request):
    return render(request, 'index.html')

@login_required
def listado_productos(request):
    productos = Producto.objects.all()
    return render(request, 'ProductosApp/ListadoProductos.html', {'productos': productos})

@login_required
def registrar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto registrado exitosamente')
            return redirect('listado_productos')
    else:
        form = ProductoForm()
    return render(request, 'ProductosApp/RegistrarProducto.html', {'form': form})

@login_required
def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'ProductosApp/DetallesProductos.html', {'producto': producto})

@login_required
def actualizar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado correctamente')
            return redirect('listado_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'ProductosApp/RegistrarProducto.html', {'form': form})

@login_required
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado exitosamente')
        return redirect('listado_productos')
    return redirect('listado_productos')
