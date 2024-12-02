Instalación
===========

Requisitos
----------
- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git

Pasos de Instalación
----------------------

1. Clonar el repositorio::

    git clone <url-del-repositorio>
    cd InventarioInDaHouse

2. Crear un entorno virtual::

    python -m venv venv
    source venv/bin/activate  # En Linux/Mac
    venv\Scripts\activate     # En Windows

3. Instalar dependencias::

    pip install -r requirements.txt

4. Configurar la base de datos::

    python manage.py makemigrations
    python manage.py migrate

5. Crear superusuario::

    python manage.py createsuperuser

6. Ejecutar el servidor::

    python manage.py runserver