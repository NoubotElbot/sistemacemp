from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('listar/',ListarAnimales.as_view(), name='listar_animal'),
    path('mis_mascotas/',ListarMisMascotas.as_view(), name='listar_mascotas'),
    path('crear/',login_required(CrearAnimal.as_view()), name='crear_animal'),
    path('editar_animal/<int:pk>',login_required(ActualizarAnimal.as_view()),name='editar_animal'),
    path('eliminar_animal/<int:pk>',login_required(EliminarAnimal.as_view()),name='eliminar_animal'),

    path('listar_tratamiento/',ListarTratamientos.as_view(),name='listar_tratamiento'),
    path('crear_tratamiento/',login_required(CrearTratamiento.as_view()), name='crear_tratamiento'),
    path('editar_tratamineto/<int:pk>',login_required(ActualizarTratamiento.as_view()),name='editar_tratamiento'),
    path('eliminar_tratamiento/<int:pk>',login_required(EliminarTratamiento.as_view()),name='eliminar_tratamiento'),
    path('listar_tratados/',ListarAnimalesTratados.as_view(),name='listar_tratados'),
    path('crear_tratado/',CrearAnimalTratado.as_view(),name='crear_tratado'),
    path('editar_tratado/<int:pk>',ActualizarAnimalTratado.as_view(),name='editar_tratado'),
    path('add-entrada/<int:pk>',AgregarSolicitud.as_view(), name='add-solicitud'),
    path('aceptar-entrada/<int:pk>',AceptarSolicitud.as_view(), name='aceptar-solicitud'),
    path('rechazar-entrada/<int:pk>',RechazarSolicitud.as_view(), name='rechazar-solicitud'),
    path('listar_solicitado/',ListarSolicitud.as_view(),name='listar_solicitados'),
    path('mis_solicitados/',ListarMiSolicitud.as_view(),name='mis_solicitados'),
    path('<int:id>/',Perfil.as_view(), name='perfil')
]