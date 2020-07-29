from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group,Permission
from .models import Usuario
# Register your models here.

class PerzonalizadoUserAdmin(UserAdmin):
    fieldsets = ()
    add_fieldsets =(
        (None,{
            'fields':('username','password1','password2'),
        }),
    )
    list_display = ('username','is_active','is_staff',)
    search_fields = ('username',)

admin.site.register(Usuario,PerzonalizadoUserAdmin)
admin.site.register(Permission)
