

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Producto, RegistroInventario
from .forms import ProductoForm, CategoriaForm, ProveedorForm, RegistroInventarioForm
import pandas as pd
from .models import Producto, Categoria, Proveedor  # Añadir Proveedor a los imports
from UsuariosApp.models import Usuario

def index(request):
    """
    Vista para la página de inicio.

    """
    return render(request, 'index.html')

@login_required
def listado_productos(request):
    """
    Vista que muestra el listado de productos con opciones de filtrado.
    
    
    Los filtros disponibles son:
    - Nombre del producto (búsqueda parcial)
    - Categoría (selección)
    """
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    
    # Filtros
    nombre_busqueda = request.GET.get('nombre', '')
    categoria_id = request.GET.get('categoria', '')
    
    if nombre_busqueda:
        productos = productos.filter(nombre__icontains=nombre_busqueda)
    
    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)
    
    context = {
        'productos': productos,
        'categorias': categorias,
        'nombre_busqueda': nombre_busqueda,
        'categoria_seleccionada': categoria_id
    }
    return render(request, 'ProductosApp/ListadoProductos.html', context)

@login_required
def registrar_producto(request):
    """
    Vista para registrar un nuevo producto.

    
    Restricciones
        - Solo usuarios con rol Gerente o Encargado pueden registrar productos
    """
    try:
        usuario_actual = Usuario.objects.get(email=request.user.email)
        # Permitir a Gerente y Encargado registrar productos
        if usuario_actual.role not in ['Gerente', 'Encargado']:
            messages.error(request, 'No tienes permisos para registrar productos')
            return redirect('listado_productos')
            
        if request.method == 'POST':
            form = ProductoForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Producto registrado exitosamente')
                return redirect('listado_productos')
        else:
            form = ProductoForm()
        return render(request, 'ProductosApp/RegistrarProducto.html', {'form': form})
    except Usuario.DoesNotExist:
        messages.error(request, 'Usuario no encontrado')
        return redirect('listado_productos')

@login_required
def detalle_producto(request, pk):
    """
    Vista que muestra los detalles de un producto específico.
    

    """
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'ProductosApp/DetallesProductos.html', {'producto': producto})

@login_required
def actualizar_producto(request, id):
    """
    Vista para actualizar la información de un producto existente.
    

    
    Restricciones
        - Solo usuarios con rol Gerente o Encargado pueden actualizar productos
    """
    try:
        usuario_actual = Usuario.objects.get(email=request.user.email)
        if usuario_actual.role not in ['Gerente', 'Encargado']:
            messages.error(request, 'No tienes permisos para actualizar productos')
            return redirect('listado_productos')
            
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
    except Usuario.DoesNotExist:
        messages.error(request, 'Usuario no encontrado')
        return redirect('listado_productos')

@login_required
def eliminar_producto(request, pk):
    """
    Vista para eliminar un producto del sistema.
    

    
    Restricciones
        - Solo usuarios con rol Gerente o Encargado pueden eliminar productos
    """
    try:
        usuario_actual = Usuario.objects.get(email=request.user.email)
        if usuario_actual.role not in ['Gerente', 'Encargado']:
            messages.error(request, 'No tienes permisos para eliminar productos')
            return redirect('listado_productos')
            
        producto = get_object_or_404(Producto, pk=pk)
        if request.method == 'POST':
            producto.delete()
            messages.success(request, 'Producto eliminado exitosamente')
            return redirect('listado_productos')
        return redirect('listado_productos')
    except Usuario.DoesNotExist:
        messages.error(request, 'Usuario no encontrado')
        return redirect('listado_productos')

@login_required
def registrar_categoria(request):
    """
    Vista para registrar una nueva categoría de productos.
    
    Restricciones
        - Solo usuarios con rol Gerente o Encargado pueden registrar categorías
    """
    try:
        usuario_actual = Usuario.objects.get(email=request.user.email)
        if usuario_actual.role not in ['Gerente', 'Encargado']:
            messages.error(request, 'No tienes permisos para registrar categorías')
            return redirect('listado_productos')
            
        if request.method == 'POST':
            form = CategoriaForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Categoría registrada exitosamente')
                return redirect('listado_productos')
        else:
            form = CategoriaForm()
        return render(request, 'ProductosApp/RegistrarCategoria.html', {'form': form})
    except Usuario.DoesNotExist:
        messages.error(request, 'Usuario no encontrado')
        return redirect('listado_productos')

@login_required
def registrar_proveedor(request):
    """
    Vista para registrar un nuevo proveedor.
    
    Restricciones
        - Solo usuarios con rol Gerente o Encargado pueden registrar proveedores
    """
    try:
        usuario_actual = Usuario.objects.get(email=request.user.email)
        if usuario_actual.role not in ['Gerente', 'Encargado']:
            messages.error(request, 'No tienes permisos para registrar proveedores')
            return redirect('listado_productos')
            
        if request.method == 'POST':
            form = ProveedorForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Proveedor registrado exitosamente')
                return redirect('listado_productos')
        else:
            form = ProveedorForm()
        return render(request, 'ProductosApp/RegistrarProveedor.html', {'form': form})
    except Usuario.DoesNotExist:
        messages.error(request, 'Usuario no encontrado')
        return redirect('listado_productos')

@login_required
def lista_registros(request):
    """
    Vista que muestra el historial de movimientos de inventario.
    
    Los registros incluyen
        - Fecha del movimiento
        - Producto afectado
        - Cantidad modificada
        - Usuario que realizó el movimiento
    """
    registros = RegistroInventario.objects.all().order_by('-fecha')
    return render(request, 'ProductosApp/registros_lista.html', {'registros': registros})

@login_required
def agregar_registro(request):
    """
    Vista para registrar un movimiento en el inventario.

    Funcionalidad
        - Actualiza el stock del producto automáticamente
        - Registra el usuario que realiza el movimiento
        - Permite seleccionar producto específico vía parámetro GET
    """
    producto_id = request.GET.get('producto_id')
    initial_data = {}
    
    if (producto_id):
        producto = get_object_or_404(Producto, id=producto_id)
        initial_data['producto'] = producto

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
            
            messages.success(request, f'Stock actualizado para {producto.nombre}')
            return redirect('listado_productos')
    else:
        form = RegistroInventarioForm(initial=initial_data)
    
    return render(request, 'ProductosApp/registro_form.html', {'form': form})

@login_required
def cargar_excel(request):
    """
    Vista para importación masiva de productos desde archivo Excel.

    Formato del Excel
        - sku: Código único del producto (str)
        - nombre: Nombre del producto (str)
        - precio: Precio unitario (float)
        - stock: Cantidad inicial (int)
        - categoria: Nombre de la categoría (str)
        - proveedor: Nombre del proveedor (str, opcional)
        - promocion: Estado de promoción (bool, opcional)
    
    Restricciones
        - Solo usuarios con rol Gerente o Encargado pueden realizar importaciones
    
    Comportamiento
        - Crea categorías y proveedores si no existen
        - Valida formato de datos
        - Reporta errores por fila si existen problemas
    """
    try:
        usuario_actual = Usuario.objects.get(email=request.user.email)
        if usuario_actual.role not in ['Gerente', 'Encargado']:
            messages.error(request, 'No tienes permisos para cargar archivos Excel')
            return redirect('listado_productos')
            
        if request.method == 'POST' and request.FILES['archivo_excel']:
            try:
                excel_file = request.FILES['archivo_excel']
                df = pd.read_excel(excel_file)
                
                # Normalizar nombres de columnas
                df.columns = [col.lower().strip() for col in df.columns]
                productos_nuevos = []
                
                for _, row in df.iterrows():
                    try:
                        # Obtener o crear la categoría
                        categoria_nombre = str(row['categoria']).strip()
                        categoria, _ = Categoria.objects.get_or_create(
                            nombre__iexact=categoria_nombre,
                            defaults={'nombre': categoria_nombre}
                        )
                        
                        # Obtener o crear el proveedor
                        if 'proveedor' in df.columns and pd.notna(row['proveedor']):
                            proveedor_nombre = str(row['proveedor']).strip()
                            proveedor, _ = Proveedor.objects.get_or_create(
                                nombre__iexact=proveedor_nombre,
                                defaults={
                                    'nombre': proveedor_nombre,
                                    'info_contacto': 'Pendiente',
                                    'direccion': 'Pendiente'
                                }
                            )
                        else:
                            proveedor = None

                        producto = Producto(
                            sku=str(row['sku']).strip(),
                            nombre=str(row['nombre']).strip(),
                            precio=float(row['precio']),
                            stock=int(row['stock']),
                            categoria=categoria,
                            proveedor=proveedor,
                            descripcion='Importado desde Excel',
                            promocion=row.get('promocion', None)
                        )
                        productos_nuevos.append(producto)
                    except KeyError as e:
                        messages.error(request, f'Error en fila {_ + 2}: Columna {e} no encontrada')
                    except Exception as e:
                        messages.error(request, f'Error en fila {_ + 2}: {str(e)}')
                        
                if productos_nuevos:
                    Producto.objects.bulk_create(productos_nuevos)
                    messages.success(request, 'Productos importados exitosamente')
                
                return redirect('listado_productos')
            except Exception as e:
                messages.error(request, f'Error al procesar el archivo: {str(e)}')
                
        return render(request, 'ProductosApp/cargar_excel.html')
    except Usuario.DoesNotExist:
        messages.error(request, 'Usuario no encontrado')
        return redirect('listado_productos')
