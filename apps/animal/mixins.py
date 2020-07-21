from django.shortcuts import redirect
from django.contrib import messages
from .models import Solicitud,Animal
class LoginYSuperUsuarioMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                return super().dispatch(request, *args, **kwargs)
        return redirect('index')
        
class ValidarSolicitudMixin(object):
    def dispatch(self, request, pk, *args, **kwargs):
        if request.user.is_authenticated:
            solicitud = Solicitud.objects.filter(animal=pk,usuario=request.user.id)
            
            if not solicitud:
                return super().dispatch(request, *args, **kwargs)
        messages.error(request, 'Ya enviaste una solicitud para ese amigo.')
        return redirect('animal:mis_solicitados')