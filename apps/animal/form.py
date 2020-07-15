from PIL import Image
from django import forms
from django.core.files import File
from .models import *
import datetime

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['nombre','especie','descripcion','fecha_nacimiento','sexo','esterilizado','fecha_llegada','peso','tamaño','id_adoptante','imagen']
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese nombre',
                    'id':'nombre'
                }
            ),
            'especie': forms.Select(
                attrs = {
                    'class':'form-control',
                    'id':'especie',
                    'required':True,
                }
            ),
            'descripcion': forms.Textarea(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese descripcion',
                    'id':'descripcion'
                }
            ),
            'fecha_nacimiento': forms.TextInput(
                attrs = {
                    'type': 'date',
                    'class':'form-control',
                    'id':'edad',
                    'min':'1980-01-01', 
                    'max': datetime.date.today(),
                }
            ),
            'sexo': forms.Select(
                attrs = {
                    'class':'form-control',
                    'id':'sexo'
                }
            ),
            'fecha_llegada': forms.TextInput(
                attrs = {
                    'type':'date',
                    'class':'form-control',
                    'id':'fecha_llegada'
                }
            ),
            'peso': forms.NumberInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese peso',
                    'id':'peso'
                }
            ),
            'tamaño': forms.Select(
                attrs = {
                    'class':'form-control',
                    'id':'tamaño'
                }
            ),
             'id_adoptante': forms.Select(
                attrs = {
                    'class':'form-control',
                    'id':'id_adoptante'
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class':'custom-file-input',
                    'id':'imagen'

                }
            )
        }

class TratamientoForm(forms.ModelForm):
    class Meta:
        model = Tratamiento
        fields = ['nombre','descripcion',]
        widgets = {
            'nombre':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese nombre',
                }
            ),
            'descripcion':forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese descripcion',
                }
            ),
        }

class TratadosForm(forms.ModelForm):
    class Meta:
        model = AnimalTratamiento
        fields = ['animal','tratamiento','fecha_tratamiento','comentario','estado',]
        widgets = {
            'animal':forms.Select(
                attrs={
                    'class':'form-control',
                    'id':'animal'
                }
            ),
            'tratamiento':forms.Select(
                attrs={
                    'class':'form-control',
                    'id':'tratamiento'
                }
            ),
            'fecha_tratamiento': forms.TextInput(
                attrs = {
                    'type':'date',
                    'class':'form-control',
                    'id':'fecha_tratamiento',
                    'min':'1980-01-01', 
                    'max': datetime.date.today(),
                }
            ),
            'comentario': forms.Textarea(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese un comentario',
                    'id':'comentario'
                }
            ),
            'estado': forms.Select(
                attrs={
                    'class':'form-control',
                    'id':'estado'
                }
            ),      
        }