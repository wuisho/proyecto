
from django.contrib import admin

from .models import Alumnos

class AlumnosAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","Matricula","Nombre","Escuela","Curso","Calificacion"]
    search_fields = ["Escuela"]
    list_editable = ["Nombre","Calificacion"]
    list_filter = ["Matricula"]
    class Meta:
        model = Alumnos


admin.site.register(Alumnos,AlumnosAdmin)
