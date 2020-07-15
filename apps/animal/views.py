from django.shortcuts import render, redirect
from .form import *
from .models import Animal, Tratamiento
from django.views.generic import View,ListView,UpdateView,CreateView,DeleteView,TemplateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.db.models import Q
from apps.animal.mixins import LoginYSuperUsuarioMixin
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
    template_name = 'tratamiento/tratamiento.html'
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
    model = AnimalTratamiento
    template_name = 'tratamiento/animales_tratados.html'
    context_object_name = 'tratados'
    queryset = AnimalTratamiento.objects.all()

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
