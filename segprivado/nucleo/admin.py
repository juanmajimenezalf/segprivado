from django.contrib import admin

from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
   fields = ['first_name', 'last_name', 'direccion', 'email', 'especialidad', 'username', 'password', 'is_medico', 'is_paciente', 'is_active' ]

# Register your models here.
admin.site.register(Usuario, UsuarioAdmin)