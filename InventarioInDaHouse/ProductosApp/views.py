from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

# Función para la página de inicio.
def index(request):
    return render(request, 'index.html')

# Función para el listado de productos.
# Se obtienen todos los productos de la base de datos y se envían al template 'ListadoProductos.html'.
def listado_productos(request):
    productos = Producto.objects.all()
    data = {'productos': productos}
    return render(request, 'ProductosApp/ListadoProductos.html', data)

# Función para registrar un producto.
# Se crea un formulario vacío para registrar un producto.
# Si el formulario es válido, se guarda el producto en la base de datos y se redirige a la lista de productos.
def registrar_producto(request):
    form = ProductoForm()
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return listado_productos(request)
    data = {'form':form}
    return render(request, 'ProductosApp/RegistrarProducto.html', data)

# Función para eliminar un producto.
# Se obtiene el producto a eliminar y se elimina de la base de datos.
# Se redirige a la lista de productos.
def eliminar_productos(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect(listado_productos)

# Función para actualizar un producto.
# Se obtiene el producto a actualizar y se crea un formulario con los datos del producto.
# Si el formulario es válido, se actualiza el producto y se redirige a la lista de productos.
def actualizar_producto(request, id):
    producto = Producto.objects.get(id=id)
    form = ProductoForm(instance=producto)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return listado_productos(request)
    data = {'form': form}
    return render(request,'ProductosApp/RegistrarProducto.html', data)
