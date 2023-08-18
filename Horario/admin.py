from django.contrib import admin

import Horario.models
from Horario.models import *

admin.site.register(Materia)
admin.site.register(Aula)
admin.site.register(Escuela)
@admin.register(Docente)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ['CODD','Names','D_Escuela']
