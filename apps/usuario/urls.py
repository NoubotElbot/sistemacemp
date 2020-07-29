from django.urls import path
from .views import ListadoUsuario, RegistrarUsuario, EliminarUsuario
urlpatterns = [
    path('listado_usuario/',ListadoUsuario.as_view(),name='listar_usuarios'),
    path('registrar_usuario/',RegistrarUsuario.as_view(),name='registrar_usuario'),
    path('eliminar_usuario/<int:pk>',EliminarUsuario.as_view(),name='eliminar_usuario'),
]