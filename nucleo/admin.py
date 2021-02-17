from django.contrib import admin
from nucleo.models import *
from nucleo.forms import CocheAdminForm


 


class ContactoInLine(admin.ModelAdmin):
    model = Contacto
    list_display = ('EmailUsuario','Atendido','Problema')
    list_filter = ('Atendido', 'EmailUsuario')
    readonly_fields = ('EmailUsuario','Problema','Texto','FechaPeticion')


class CochelInLine(admin.ModelAdmin):
    model = Coche
    form = CocheAdminForm
    list_filter = ('Matricula','FechaMatriculacion')
    list_display = ('Matricula','FechaMatriculacion')

   
    


class ReparacionlInLine(admin.ModelAdmin):
    model = Reparacion    
    verbose_name ='Reparaciones'
    list_filter = ('Arreglado', 'FechaSolicitud','FechaArreglo')
    list_display = ('Arreglado','FechaSolicitud','FechaArreglo','Coches')

class NoticialInLine(admin.ModelAdmin):
    model = Noticia    
    verbose_name_plural ='Noticias'
    list_display = ('FechaCreacion','Creador')
    list_filter = ('FechaCreacion',)
    readonly_fields = ('FechaCreacion','Creador')

  
        

admin.site.register(Contacto, ContactoInLine)
admin.site.register(Noticia, NoticialInLine)
admin.site.register(Reparacion, ReparacionlInLine)
admin.site.register(Coche,CochelInLine)
