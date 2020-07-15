from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

# Create your models here.
class UsuarioManager(BaseUserManager):
    def create_user(self,email,username,nombres,password = None):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')
        user = self.model(
            username = username,
            email = self.normalize_email(email),
            nombres = nombres,
        )

        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,username,email,nombres,password):
        user = self.create_user(
            email,
            username=username,
            nombres=nombres,
            password=password
        )
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

class Usuario(AbstractBaseUser,PermissionsMixin):
    id = models.AutoField(primary_key=True)
    username = models.CharField('Nombre de usuario', unique = True, max_length=100)
    email = models.EmailField('Correo Electrónico', max_length=50, unique = True)
    nombres = models.CharField('Nombres', max_length=100, blank=True,null = True)
    apellidos = models.CharField('Apellidos',max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default = True) 
    is_staff = models.BooleanField('Es staff',default=False)
    object = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','nombres']

    def __str__(self):
        return self.username
    
    def has_perm(self,perm,obj = None):
        return True
    
    def has_module_perms(self,app_label):
        return True