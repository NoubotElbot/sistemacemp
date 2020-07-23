from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .mixins import LoginYSuperUsuarioMixin
from .models import Usuario
from .form import FormularioLogin, FormularioUsuario
# Create your views here.

class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('index')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self,request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request, *args, **kwargs)
    def form_valid(self, form):
        login(self.request,form.get_user())
        return super(Login,self).form_valid(form)

def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login')

class ListadoUsuario(LoginYSuperUsuarioMixin,ListView):
    model = Usuario
    template_name = 'usuario/listar_usuarios.html'
    def get_queryset(self):
        return self.model.object.all()

class RegistrarUsuario(LoginYSuperUsuarioMixin,CreateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'usuario/crear_usuario.html'
    success_url = reverse_lazy('usuarios:listar_usuarios')

class EditarUsuario(LoginYSuperUsuarioMixin,UpdateView):
    model = Usuario
    template_name = 'usuario/crear_usuario.html'
    form_class = FormularioUsuario
    success_url = reverse_lazy('usuarios:listar_usuarios')

class EliminarUsuario(LoginYSuperUsuarioMixin,DeleteView):
    model = Usuario

    def post(self,request,pk,*args,**kwargs):
        object = get_object_or_404(Usuario,id = pk)
        object.is_active = False
        object.save()
        return redirect('usuarios:listar_usuarios')
