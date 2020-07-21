from django.shortcuts import render, redirect
from .form import AnimalForm, TratamientoForm, TratadosForm
from .models import Animal, Tratamiento, AnimalTratamiento, Solicitud, EstadosSolicitud
from django.views.generic import View,ListView,UpdateView,CreateView,DeleteView,TemplateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .mixins import LoginYSuperUsuarioMixin, ValidarSolicitudMixin
# Create your views here.
 
# class ListarAnimales(ListView):
#     model = Animal
#     template_name = 'animal/listar_animal.html'
#     context_object_name = 'animales'
#     queryset = Animal.objects.filter(activo=True)


def listarAnimales(request):
    queryset = request.GET.get("buscar")
    animales = Animal.objects.filter(activo=True)
    if queryset:
        animales = Animal.objects.filter(activo=True, nombre__icontains=queryset)
    return render(request,'animal/listar_animal.html',{'animales':animales})


def listarMisMascotas(request,id):
    queryset = request.GET.get("buscar")
    animales = Animal.objects.filter(activo=True, id_adoptante=id)
    if queryset:
        animales = Animal.objects.filter(activo=True, nombre__icontains=queryset, id_adoptante=id)
    return render(request,'animal/listar_mascotas.html',{'animales':animales})

class ListarTratamientos(LoginYSuperUsuarioMixin,ListView):
    model = Tratamiento
    template_name = 'tratamiento/listar_tratamientos.html'
    context_object_name = 'tratamientos'
    queryset = Tratamiento.objects.filter(activo=True)

class CrearTratamiento(LoginYSuperUsuarioMixin,CreateView):
    model = Tratamiento
    template_name = 'tratamiento/crear_tratamiento.html'
    form_class = TratamientoForm
    success_url = reverse_lazy('animal:listar_tratamiento')

class ActualizarTratamiento(LoginYSuperUsuarioMixin,UpdateView):
    model = Tratamiento
    template_name = 'tratamiento/crear_tratamiento.html'
    form_class = TratamientoForm
    success_url = reverse_lazy('animal:listar_tratamiento')

class EliminarTratamiento(LoginYSuperUsuarioMixin,DeleteView):
    model = Tratamiento

    def post(self,request,pk,*args,**kwargs):
        object = get_object_or_404(Tratamiento,id = pk)
        object.activo = False
        object.save()
        return redirect('animal:listar_tratamiento')

class ListarAnimalesTratados(LoginYSuperUsuarioMixin,ListView):
    template_name = 'tratamiento/animales_tratados.html'
    def get(self,request,*args,**kwargs):
        tratados = AnimalTratamiento.objects.all()
        animales = Animal.objects.filter(animaltratamiento__isnull=False).distinct()
        return render(request,self.template_name,{'animales':animales,'tratados':tratados})

class CrearAnimalTratado(LoginYSuperUsuarioMixin,CreateView):
    model = AnimalTratamiento
    template_name = 'tratamiento/crear_tratado.html'
    form_class = TratadosForm
    success_url = reverse_lazy('animal:listar_tratados')

class ActualizarAnimalTratado(LoginYSuperUsuarioMixin,UpdateView):
    model = AnimalTratamiento
    template_name = 'tratamiento/crear_tratado.html'
    form_class = TratadosForm
    success_url = reverse_lazy('animal:listar_tratados')

class CrearAnimal(LoginYSuperUsuarioMixin,CreateView):
    model = Animal
    template_name = 'animal/crear_animal.html'
    form_class = AnimalForm
    success_url = reverse_lazy('animal:listar_animal')
# def crearAnimal(request):
#     if request.method == 'POST':
#         animal_form = AnimalForm(request.POST, request.FILES)
#         if animal_form.is_valid():
#             animal_form.save()
#             return redirect('animal:listar_animal')
#     else:
#         animal_form = AnimalForm()
#     return render(request,'animal/crear_animal.html',{'form':animal_form})

class ActualizarAnimal(LoginYSuperUsuarioMixin,UpdateView):
    model = Animal
    template_name = 'animal/crear_animal.html'
    form_class = AnimalForm
    success_url = reverse_lazy('animal:listar_animal')

class EliminarAnimal(LoginYSuperUsuarioMixin,DeleteView):
    model = Animal

    def post(self,request,pk,*args,**kwargs):
        object = get_object_or_404(Animal,id = pk)
        object.activo = False
        object.save()
        return redirect('animal:listar_animal')

def perfil(request,id):
    animal_perfil = get_object_or_404(Animal,id = id)
    return render(request, 'animal/perfil.html',{'animal': animal_perfil})

class AgregarSolicitud(ValidarSolicitudMixin, View):

    def post(self,request,*args,**kwargs):
        usuario = self.request.user
        login_url = reverse_lazy('usuario:login')
        entrada = Animal.objects.get(id=self.kwargs['pk'])
        estado= EstadosSolicitud.objects.get(id="3")
        Solicitud.objects.create(
            usuario=usuario,
            animal=entrada,
            estado_solicitud=estado
        )
        return redirect(
                'animal:listar_solicitados',
            )
    

class AceptarSolicitud(LoginYSuperUsuarioMixin,UpdateView ):
    model = Solicitud

    def post(self,request,pk,*args,**kwargs):
        adop= Solicitud.objects.get(id=self.kwargs['pk'])
        mascota= adop.animal.id
        adoptante=adop.usuario.id
        estado= EstadosSolicitud.objects.get(id="1")
        Solicitud.objects.filter(id=self.kwargs['pk']).update(
            estado_solicitud=estado
        )
        Animal.objects.filter(id=mascota).update(
            id_adoptante=adoptante
        )
        
        return redirect(
                'animal:listar_solicitados',
            )
    

class RechazarSolicitud(LoginYSuperUsuarioMixin,UpdateView ):
    model = Solicitud

    def post(self,request,pk,*args,**kwargs):
        object = get_object_or_404(Solicitud,id = pk)
        estado= EstadosSolicitud.objects.get(id="2")
        object.estado_solicitud = estado
        object.save()
        return redirect('animal:listar_solicitados')

class ListarSolicitud(LoginYSuperUsuarioMixin,ListView):
    template_name = 'solicitud/animales_solicitados.html'

    def get(self, request, *args, **kwargs):
        solicitudes = Solicitud.objects.all()
        # animales = Animal.objects.raw('SELECT distinct animal.* FROM animal inner join solicitud on animal.id = solicitud.animal_id;')
        animales = Animal.objects.filter(solicitud__isnull = False).distinct()
        return render(request,self.template_name,{'solicitados': solicitudes, 'animales': animales})