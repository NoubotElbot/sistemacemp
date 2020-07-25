from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class animalResources(resources.ModelResource):
    class Meta:
        model = Animal

class animalesAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('id','nombre','descripcion','especie','fecha_nacimiento','sexo','esterilizado','id_adoptante','tamaño','peso','activo','imagen')
    resources_class = animalResources
    
admin.site.register(Animal,animalesAdmin)

class tratamientoResource(resources.ModelResource):
    class Meta:
        model = Tratamiento

class tratamientoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('id','nombre','descripcion','activo')
    resources_class = tratamientoResource

admin.site.register(Tratamiento,tratamientoAdmin)

class animalTratamientoResource(resources.ModelResource):
    class Meta:
        model = AnimalTratamiento

class animalTratamientoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['fecha_tratamiento']
    list_display = ('id','fecha_tratamiento','animal','tratamiento','comentario',)
    resources_class = animalTratamientoResource

admin.site.register(AnimalTratamiento,animalTratamientoAdmin)

class especieResources(resources.ModelResource):
    class Meta:
        model = Especie

class especiesAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre_especie']
    list_display = ('id','nombre_especie','activo')
    resources_class = especieResources

admin.site.register(Especie,especiesAdmin)

class solicitudResources(resources.ModelResource):
    class Meta:
        model = Solicitud

class solicitudesAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre_solicitud']
    list_display = ('id','usuario','animal','fecha_solicitud','estado_solicitud')
    resources_class = solicitudResources

admin.site.register(Solicitud,solicitudesAdmin)

class estadossolicitudResource(resources.ModelResource):
    class Meta:
        model = EstadosSolicitud

class estadossolicitudAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre_estadossolicitud']
    list_display = ('id','nombre_estado','descripcion')
    resources_class = estadossolicitudResource

admin.site.register(EstadosSolicitud,estadossolicitudAdmin)

class publicacionesResource(resources.ModelResource):
    class Meta:
        model = Publicacion

class publicacionAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id','usuario','animal','fecha_publicacion','descripcion')
    resources_class = publicacionesResource

admin.site.register(Publicacion,publicacionAdmin)

class imagenResource(resources.ModelResource):
    class Meta:
        model = ImagenPublicacion

class imagenAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id','ruta_imagen','publicacion')
    resources_class = imagenResource

admin.site.register(ImagenPublicacion,imagenAdmin)