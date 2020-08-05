from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

# Create your models here.
class UsuarioManager(BaseUserManager):
    def _create_user(self,rut,username,email,nombres,apellidos,password,is_staff,is_superuser,**extra_fields):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')
        user = self.model(
            rut = rut,
            username = username,
            email = self.normalize_email(email),
            nombres = nombres,
            apellidos = apellidos,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_user(self,rut,username,email,nombres,apellidos,password = None,**extra_fields):
        return self._create_user(rut,username,email,nombres,apellidos,password,False,False,**extra_fields)
    def create_superuser(self,rut,username,email,nombres,apellidos,password = None,**extra_fields):
        return self._create_user(rut,username,email,nombres,apellidos,password,True,True,**extra_fields)

class Usuario(AbstractBaseUser,PermissionsMixin, models.Model):
    id = models.AutoField(primary_key=True)
    rut = models.CharField('Rut', unique = True, max_length=12)
    username = models.CharField('Nombre de usuario', unique = True, max_length=100)
    email = models.EmailField('Correo Electrónico', max_length=50, unique = True)
    direccion = models.CharField('Dirección', max_length=100, blank=True, null = True)
    nombres = models.CharField('Nombres', max_length=100, blank=False, null = False)
    apellidos = models.CharField('Apellidos',max_length=100, blank=False, null=False)
    fecha_nacimiento = models.DateField('Fecha de nacimiento', blank=False, null=True)
    telefono = models.IntegerField('Teléfono',blank=True, null=True)
    is_active = models.BooleanField(default = True) 
    is_staff = models.BooleanField(default=False)
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','rut','nombres','apellidos']

    def __str__(self):
        return self.username

    def getEdad(self):
        años = (datetime.date.today() - self.fecha_nacimiento).days / 365.25
        return int(años)