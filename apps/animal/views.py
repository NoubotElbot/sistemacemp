from django.shortcuts import render, redirect
from .form import AnimalForm, TratamientoForm, TratadosForm, PostForm, ImageForm
from .models import Animal, Tratamiento, AnimalTratamiento, Solicitud, EstadosSolicitud, ImagenPublicacion, Publicacion
from django.views.generic import View,ListView,UpdateView,CreateView,DeleteView,TemplateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.forms import modelformset_factory
from .mixins import LoginYSuperUsuarioMixin, ValidarSolicitudMixin
# Create your views here.
 
class ListarAnimales(ListView):
    template_name = 'animal/listar_animal.html'
    def get(self, request, *args, **kwargs):
        queryset = request.GET.get("buscar")
        animales = Animal.objects.filter(activo=True)
        if queryset:
            animales = Animal.objects.filter(activo=True, nombre__icontains=queryset)
        return render(request,self.template_name,{'animales':animales})

class ListarMisMascotas(ListView):
    template_name = 'animal/listar_mascotas.html'
    def get(self, request, *args, **kwargs):
        queryset = request.GET.get("buscar")
        animales = Animal.objects.filter(activo=True, id_adoptante=request.user.id)
        if queryset:
            animales = Animal.objects.filter(activo=True, nombre__icontains=queryset, id_adoptante=request.user.id)
        return render(request,self.template_name,{'animales':animales})

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

# def perfil(request,id):
#     animal_perfil = get_object_or_404(Animal,id = id)
#     return render(request, 'animal/perfil.html',{'animal': animal_perfil})

def perfil(request,id):
        ImageFormSet = modelformset_factory(ImagenPublicacion,form=ImageForm, extra=3)
        if request.method == 'POST':
            postForm = PostForm(request.POST)
            formset = ImageFormSet(request.POST, request.FILES, queryset=ImagenPublicacion.objects.none())
            if postForm.is_valid() and formset.is_valid():

                post_form = postForm.save(commit=False)
                post_form.usuario = request.user
                post_form.animal = Animal.objects.get(id=id)
                post_form.save()
                for form in formset.cleaned_data:
                    if form:
                        image = form['ruta_imagen']
                        photo = ImagenPublicacion(publicacion=post_form, ruta_imagen=image)
                        photo.save()
                return redirect('animal:perfil',id = id)
            else:
                print(postForm.errors, formset.errors)
        else:
            postForm = PostForm()
            formset = ImageFormSet(queryset = ImagenPublicacion.objects.none())
            animal_perfil = get_object_or_404(Animal,id = id)
            publicacion = Publicacion.objects.filter(animal=id)
            imagen_p = ImagenPublicacion.objects.filter(publicacion__id__in=publicacion)
        return render(request, 'animal/perfil.html', {'postForm': postForm, 'formset': formset, 'animal': animal_perfil, 'publicacion': publicacion,'imagen':imagen_p})

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
                'animal:mis_solicitados',
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

class ListarMiSolicitud(LoginRequiredMixin,ListView):
    template_name = 'solicitud/mis_solicitados.html'

    def get(self, request, *args, **kwargs):
        solicitudes = Solicitud.objects.filter(usuario = request.user.id)
        return render(request,self.template_name,{'solicitados': solicitudes}) 