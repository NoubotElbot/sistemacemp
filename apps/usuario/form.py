from django import forms
from django.contrib.auth.forms import AuthenticationForm
from apps.usuario.models import Usuario
import datetime

class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'

class FormularioUsuario(forms.ModelForm):
    password1 = forms.CharField(label = 'Contraseña', widget = forms.PasswordInput(
        attrs = {
            'class':'form-control',
            'placeholder':'Ingrese su contraseña...',
            'id':'password1',
            'required':'required',
        }
    ))
    password2 = forms.CharField(label = 'Contraseña de Confirmación', widget = forms.PasswordInput(
        attrs = {
            'class':'form-control',
            'placeholder':'Ingrese nuevamente su contraseña...',
            'id':'password2',
            'required':'required',
        }
    ))

    class Meta:
        model = Usuario
        fields = ['rut','username','email','nombres','apellidos','direccion','fecha_nacimiento','telefono']
        widgets = {
            'rut': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese su Rut',
                    'id':'rut',
                    'name':'rut',
                    'oninput':"checkRut(this)"
                }
            ),
            'username': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese su nombre de usuario',
                    'id':'username'
                }
            ),
            'email': forms.EmailInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese su correo electrónico',
                }
            ),
            'nombres': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese sus nombres',
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese sus apellidos',
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su direccion',
                }
            ),
            'fecha_nacimiento': forms.TextInput(
                attrs = {
                    'type': 'date',
                    'class':'form-control',
                    'id':'edad',
                    'min':'1900-01-01', 
                    'max': datetime.date.today(),
                }
            ),
            'telefono': forms.NumberInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese su teléfono',
                    'id':'telefono',
                    'max':'99999999'
                }
            )

        }
    def clean_password2(self):
        contraseña = self.cleaned_data.get('password1')
        contraseña_con = self.cleaned_data.get('password2')
        if contraseña != contraseña_con:
            raise forms.ValidationError('Contraseñas no coinciden!')
        return contraseña
    def save(self,commit = True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
