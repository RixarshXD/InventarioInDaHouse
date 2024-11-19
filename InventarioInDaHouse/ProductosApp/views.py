from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Producto, RegistroInventario
from .forms import ProductoForm, CategoriaForm, ProveedorForm, RegistroInventarioForm
import pandas as pd
from .models import Producto, Categoria

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

@login_required
def registrar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría registrada exitosamente')
            return redirect('listado_productos')
    else:
        form = CategoriaForm()
    return render(request, 'ProductosApp/RegistrarCategoria.html', {'form': form})

@login_required
def registrar_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Proveedor registrado exitosamente')
            return redirect('listado_productos')
    else:
        form = ProveedorForm()
    return render(request, 'ProductosApp/RegistrarProveedor.html', {'form': form})

@login_required
def lista_registros(request):
    registros = RegistroInventario.objects.all().order_by('-fecha')
    return render(request, 'ProductosApp/registros_lista.html', {'registros': registros})

@login_required
def agregar_registro(request):
    if request.method == 'POST':
        form = RegistroInventarioForm(request.POST)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.usuario = request.user
            registro.save()
            
            # Actualizar el stock del producto
            producto = registro.producto
            producto.stock += registro.cantidad
            producto.save()
            
            return redirect('lista_registros')
    else:
        form = RegistroInventarioForm()
    return render(request, 'ProductosApp/registro_form.html', {'form': form})

@login_required
def cargar_excel(request):
    if request.method == 'POST' and request.FILES['archivo_excel']:
        try:
            excel_file = request.FILES['archivo_excel']
            df = pd.read_excel(excel_file)
            productos_nuevos = []
            
            for _, row in df.iterrows():
                try:
                    categoria, _ = Categoria.objects.get_or_create(nombre=row['categoria'])
                    producto = Producto(
                        sku=row['SKU'],
                        nombre=row['Nombre'],
                        precio=row['precio'],
                        stock=row['stock'],
                        categoria=categoria,
                        descripcion='Importado desde Excel'
                    )
                    productos_nuevos.append(producto)
                except Exception as e:
                    messages.error(request, f'Error en fila {_ + 2}: {str(e)}')
                    
            if productos_nuevos:
                Producto.objects.bulk_create(productos_nuevos)
                messages.success(request, 'Productos importados exitosamente')
            
            return redirect('listado_productos')
        except Exception as e:
            messages.error(request, f'Error al procesar el archivo: {str(e)}')
            
    return render(request, 'ProductosApp/cargar_excel.html')
