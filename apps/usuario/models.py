from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

# Create your models here.
class UsuarioManager(BaseUserManager):
    def _create_user(self,username,email,nombres,password,is_staff,is_superuser,**extra_fields):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')
        user = self.model(
            username = username,
            email = self.normalize_email(email),
            nombres = nombres,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_user(self,username,email,nombres,password = None,**extra_fields):
        return self._create_user(username,email,nombres,password,False,False,**extra_fields)
    def create_superuser(self,username,email,nombres,password = None,**extra_fields):
        return self._create_user(username,email,nombres,password,True,True,**extra_fields)

class Usuario(AbstractBaseUser,PermissionsMixin, models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField('Nombre de usuario', unique = True, max_length=100)
    email = models.EmailField('Correo Electrónico', max_length=50, unique = True)
    nombres = models.CharField('Nombres', max_length=100, blank=True,null = True)
    apellidos = models.CharField('Apellidos',max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default = True) 
    is_staff = models.BooleanField(default=False)
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','nombres']

    def __str__(self):
        return self.username