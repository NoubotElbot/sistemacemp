from django.db import models
from apps.usuario.models import Usuario
from PIL import Image

import datetime

##########  MODELO TRATAMIENTO ##########
class Tratamiento(models.Model):
    id          = models.AutoField(primary_key=True)
    nombre      = models.CharField("Nombre Tratamiento",max_length=50,blank=False,null=False)
    descripcion = models.TextField("Descripcion",max_length=200,blank=False,null=False)
    activo      = models.BooleanField("Activo",blank=False,null=False, default=True)
    create_at   = models.DateTimeField("Creacion registro",auto_now_add=True)
    update_at   = models.DateTimeField("Ultima modificacion",auto_now=True)

    class Meta:
        db_table = 'TRATAMIENTO'
        verbose_name = "Tratamiento"
        verbose_name_plural = "Tratamientos"
    
    def __str__(self):
        return self.nombre

########## MODELO ESPECIES ##########

class Especie(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_especie = models.CharField("Especie", max_length=30 ,blank=False, null=False,)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    activo = models.BooleanField("Activo", blank=False,null=False, default=True)

    class Meta:
        db_table = 'ESPECIE'
        verbose_name = "Especie"
        verbose_name_plural = "Especies"

    def __str__(self):
        return self.nombre_especie

########## MODELO ANIMAL ##########
class Animal(models.Model):
    SEXO = (
            ('Macho','Macho'),
            ('Hembra','Hembra'),
        )
    TAMAÑO = (
        ('Pequeño','Pequeño'),
        ('Mediano','Mediano'),
        ('Grande','Grande'),
    )
    id                  = models.AutoField(primary_key=True)
    nombre              = models.CharField("Nombre",max_length=50, blank=False, null=False)
    descripcion         = models.TextField("Descripcion del animal",max_length=350,blank=True,null=True)
    fecha_nacimiento    = models.DateField("Fecha nacimiento", blank=False, null=False)
    sexo                = models.CharField("Sexo", max_length=10, blank=False, null=False, choices=SEXO)
    tamaño              = models.CharField("Tamaño", max_length=10, blank=False, null=False, choices=TAMAÑO)
    esterilizado        = models.BooleanField("Esterilizado", blank=False, null=False, default=False)
    fecha_llegada       = models.DateField("Fecha de llegada a la sede", auto_now=False, auto_now_add=False)
    peso                = models.DecimalField("Peso kg", max_digits=4, decimal_places=2)
    especie             = models.ForeignKey(Especie, on_delete=models.SET_NULL, blank=True, null=True)
    id_adoptante        = models.ForeignKey(Usuario, on_delete=models.SET_NULL, blank=True, null=True)
    activo              = models.BooleanField("Activo",blank=False,null=False,default=True)
    create_at           = models.DateTimeField("Creacion registro",auto_now_add=True)
    update_at           = models.DateTimeField("Ultima modificacion",auto_now=True)
    imagen              = models.ImageField(upload_to="imagen", null=True,blank=True)

    def getEdad(self):
        años = (datetime.date.today() - self.fecha_nacimiento).days / 365.25
        meses = (años - int(años))*12
        return int(años), int(meses)
            
    def save(self, *args, **kwargs):
        try:
            super().save(*args, **kwargs)
            img  = Image.open(self.imagen.path)
            
            if img.height > 300 or img.width > 300:
                output_size = (300,300)
                img.thumbnail(output_size)
                img.save(self.imagen.path)
        except:
            print("no hay foto")
        
    class Meta:
        db_table = 'ANIMAL'
        verbose_name = "Animal"
        verbose_name_plural = "Animales"

    def __str__(self):
        return str(self.id)+"# "+self.nombre

########## MODELO ANIMALES TRATADOS ##########
class AnimalTratamiento(models.Model):
    ESTADO_TRATAMIENTO = (
        ('Vigente','Vigente'),
        ('Concluido','Concluido'),
    )

    animal              = models.ForeignKey(Animal, on_delete=models.CASCADE)
    tratamiento         = models.ForeignKey(Tratamiento, on_delete=models.CASCADE)
    fecha_tratamiento   = models.DateField("Fecha de aplicacion",auto_now=False, auto_now_add=False)
    comentario          = models.TextField("Comentario",max_length=200,blank=True)
    estado              = models.CharField("Estado tratamiento", max_length=10,blank=False, null=False, choices=ESTADO_TRATAMIENTO, default="Vigente")

    class Meta:
        db_table = 'ANIMAL_TRATAMIENTO'
        unique_together = (('animal','tratamiento','fecha_tratamiento'),)
        verbose_name = "Animal tratamiento"
        verbose_name_plural = "Animales tratados"

########## MODELO PUBLICACIONES ##########

class Publicacion(models.Model):
    id                = models.AutoField(primary_key=True)
    usuario           = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    animal            = models.ForeignKey(Animal, on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    descripcion       = models.TextField(max_length=400,blank=True)
    activo            = models.BooleanField("Activo",blank=False,null=False,default=True)
    class Meta:
        db_table = 'PUBLICACION'
        verbose_name = "Publicacion"
        verbose_name_plural = "Publicaciones"
    def __str__(self):
        return str(self.id)

class ImagenPublicacion(models.Model):
    ruta_imagen = models.ImageField(upload_to="publicacion", null=True,blank=True)
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    class Meta:
        db_table = 'IMAGEN_PUBLICACION'
        verbose_name = "Imagen Publicacion"
        verbose_name_plural = "Imagenes Publicaciones"

######SOLICITUDES

class EstadosSolicitud(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_estado = models.CharField(max_length = 15, blank=False, null=False)
    descripcion = models.CharField(max_length = 200, blank=False, null=False)

    class Meta:
        db_table = 'ESTADO_SOLICITUD'
        verbose_name = "Estado solicitud"
        verbose_name_plural = "Estados de solicitudes"
    
    def __str__(self):
        return self.nombre_estado

class Solicitud(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    fecha_solicitud = models.DateTimeField("Fecha Solicitud",auto_now_add=True)
    estado_solicitud = models.ForeignKey(EstadosSolicitud, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'SOLICITUD'
        verbose_name = "Solicitud Animal"
        verbose_name_plural = "Solicitudes Animales"
