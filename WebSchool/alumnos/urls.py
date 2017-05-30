from django.conf.urls import url
from django.contrib import admin
from alumnos import views
from alumnos.views import (ListaDeAlumnos, DetalleDeAlumnos, RegistrarAlumnos, ActualizarAlumno)

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', DetalleDeAlumnos.as_view(), name='detalle'),
    url(r'^registrar/$', RegistrarAlumnos.as_view(), name='registrar'),
    url(r'^lista/$', ListaDeAlumnos.as_view(), name='lista'),
    url(r'^editar/(?P<slug>[\w-]+)/$', ActualizarAlumno.as_view(), name='detalle_slug'),
    ]
