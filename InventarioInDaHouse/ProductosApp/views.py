from django.shortcuts import render
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
