from django.urls import path, include
from .views import listado_usuarios, registrar_usuario, actualizar_usuario, eliminar_usuario, loginUsuario, logoutUsuario
from .api import UsuarioViewSet
from rest_framework import routers 

router = routers.DefaultRouter()
router.register('usuarios', UsuarioViewSet, 'usuarios')


urlpatterns = [
    path('login/', loginUsuario, name='login'),
    path('logout/', logoutUsuario, name='logout'),
    path('', listado_usuarios, name='listado'),
    path('registrar/', registrar_usuario, name='registrar/usuario'),
    path('actualizar_usuario/<int:id>/', actualizar_usuario, name='actualizar_usuario'),
    path('eliminar_usuario/<int:id>/', eliminar_usuario, name='eliminar_usuario'),
    
    # URL API
    path('api/', include(router.urls), name='api'),
]


