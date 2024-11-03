from django.urls import path
from .views import listado_productos, registrar_roducto

urlpatterns = [
    path('', listado_productos, name='listado'),
    path('registrar/',registrar_roducto , name='registrar'),
]
