.. InDaHouse documentation master file

Documentación del Sistema de Inventario InDaHouse
=================================================

Bienvenido a la documentación del sistema de inventario InDaHouse, una aplicación web desarrollada en Django para la gestión de inventarios.

.. toctree::
   :maxdepth: 2
   :caption: Contenidos:

   instalacion
   modulos


Índices y Tablas
----------------

* :ref:`genindex`
* :ref:`modindex`


Instalación
------------

1. Clonar el repositorio
2. Crear un entorno virtual
3. Instalar dependencias::

    pip install -r requirements.txt

4. Ejecutar migraciones::

    python manage.py migrate

5. Crear superusuario::

    python manage.py createsuperuser

Módulos Principales
--------------------

UsuariosApp
~~~~~~~~~~~~

Gestión de usuarios y autenticación del sistema.

Modelos
^^^^^^^

Usuario
'''''''
.. py:class:: Usuario(AbstractUser)

   Modelo personalizado que extiende AbstractUser para gestión de usuarios.

   **Atributos principales:**

   - email: Identificador único del usuario
   - role: Rol del usuario (Gerente/Vendedor/Encargado)
   - rut: RUT chileno del usuario

   **Roles disponibles:**
   
   - Gerente: Acceso total al sistema
   - Encargado: Gestión de inventario
   - Vendedor: Consulta de productos

Vistas
^^^^^^

.. py:function:: loginUsuario(request)

   Autentica usuarios usando email y contraseña.

.. py:function:: registrar_usuario(request)

   Permite a usuarios con rol Gerente crear nuevos usuarios.

.. py:function:: listado_usuarios(request)

   Muestra listado de usuarios para roles Gerente y Encargado.

ProductosApp
~~~~~~~~~~~~

Gestión del inventario y productos.

Modelos
^^^^^^^

Producto
''''''''
.. py:class:: Producto

   Modelo principal para gestión de productos en inventario.

   **Atributos principales:**

   - nombre: Nombre del producto
   - descripcion: Descripción detallada
   - precio: Precio unitario
   - stock: Cantidad disponible
   - sku: Código único
   - categoria: Categoría del producto
   - proveedor: Proveedor asociado
   - promocion: Estado de promoción

Categoria
'''''''''
.. py:class:: Categoria

   Clasificación de productos.

   **Atributos:**
   
   - nombre: Nombre de la categoría
   - descripcion: Descripción opcional

RegistroInventario
~~~~~~~~~~~~~~~~~~

.. py:class:: RegistroInventario

   Registro de movimientos en inventario.

   **Atributos:**

   - usuario: Usuario que realiza el movimiento
   - producto: Producto afectado
   - cantidad: Cantidad modificada
   - fecha: Fecha del registro

Vistas Principales
~~~~~~~~~~~~~~~~~~

.. py:function:: listado_productos(request)

   Muestra catálogo de productos con filtros.

.. py:function:: registrar_producto(request)

   Permite a Gerentes y Encargados agregar productos.

.. py:function:: cargar_excel(request)

   Importación masiva de productos desde Excel.

Formularios
~~~~~~~~~~~

ProductoForm
~~~~~~~~~~~~

.. py:class:: ProductoForm

   Formulario para crear y editar productos.

   **Validaciones:**

   - Nombre: Solo letras
   - Precio: No negativo
   - Categoría: Obligatoria
   - Promoción: Estado válido requerido

RegistroInventarioForm
~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: RegistroInventarioForm

   Registra movimientos de inventario.

