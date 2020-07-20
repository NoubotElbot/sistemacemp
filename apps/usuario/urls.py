from django.urls import path
from apps.usuario.views import ListadoUsuario, RegistrarUsuario
urlpatterns = [
    path('listado_usuario/',ListadoUsuario.as_view(),name='listar_usuarios'),
    path('registrar_usuario/',RegistrarUsuario.as_view(),name='registrar_usuario'),
]