from django.views.generic.edit import CreateView, UpdateView
from django.db.models import Q
from WebSchool.multipleslug import MultiSlugMixin
from .models import Alumnos
import os
from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .forms import AlumnosAddForm, AlumnosModelForm
from .models import Alumnos
from django.conf import settings
from mimetypes import guess_type
from wsgiref.util import FileWrapper

def home(request):
    context=locals();
    template='home.html'
    return render(request, template, context)

class ActualizarAlumno(MultiSlugMixin, UpdateView):
    model = Alumnos
    form_class = AlumnosModelForm
    success_url = "/alumnos/lista/"

    def get_context_data(self, *args, **kwargs):
        context = super(ActualizarAlumno, self).get_context_data(*args, **kwargs)
        context["submit_btn"]="Actualizar"
        return context

class DetalleDeAlumnos(DetailView):
    model = Alumnos

class ListaDeAlumnos(ListView):
    model = Alumnos


class RegistrarAlumnos(CreateView):
    model = Alumnos
    form_class = AlumnosModelForm
    success_url = "/alumnos/lista/"

    def get_context_data(self, *args, **kwargs):
        context = super(RegistrarAlumnos, self).get_context_data(*args, **kwargs)
        context["submit_btn"]="Registrar"
        return context

def lista_alumnos(request):
    alum = Alumnos.objects.all()
    print request
    mens = "Alumnos Registrados Actualmente"
    template = "listaDeAlumnos.html"
    contexto= {"Mensaje": mens,
               "Alumnos": alum }
    return render(request, template, contexto)

def inicio(request):
    alum = Alumnos.objects.all()
    mens = "Hola"
    print request
    template = "base.html"
    contexto= {"Mensaje": mens,
               "Alumnos": alum }
    return render(request, template, contexto)

def detalle_slug(request, slug=None):
    #Logico de negocio alias hechizo
    print "hola"
    try:
        alumnos = get_object_or_404(Libros, slug=slug)
    except Alumnos.MultipleObjectsReturned:
        alumnos = Alumnos.objects.filter(slug=slug).order_by("-Matricula").first()

    print libros
    m = "Alumnos"
    template = "detalle_slug.html"
    contexto= {"mensaje":m,
           "Alumnos": alumnos }
    return render(request, template, contexto)

def detalle_s(request, slug=None):
    #Logico de negocio alias hechizo
    try:
        alumnos = get_object_or_404(Producto, slug=slug)
    except Alumnos.MultipleObjectsReturned:
        alumnos = Alumnos.objects.filter(slug=slug).order_by("-Matricula").first()
    m = "Alumnos"
    template = "detalle_slug.html"
    contexto= {"mensaje":m,
           "Alumnos": alumnos }
    return render(request, template, contexto)


def actualizar(request, object_id=None):

    alumnos = get_object_or_404(Alumnos, id=object_id)
    form = AlumnosModelForm(request.POST or None, instance=alumnos)
    if form.is_valid():
        form.save()
        print "Actualizacion exitosa!"
    template = "actualizar.html"
    contexto= {
           "Alumnos": alumnos,
           "form":form,
           "titulo":"Actualizar Alumno"
           }
    return render(request, template, contexto)

def detalle_alumno(request, object_id=None):

    alum = get_object_or_404(Alumnos, id=object_id)
    mens = "Alumnos Registrados Actualmente"
    template = "detalle_alumno.html"
    contexto= {"Mensaje":mens,
           "Alumnos": alum }
    return render(request, template, contexto)


def agregar_alumno(request):
    form = AlumnosModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        print "Alta exitosa!"
    template = "agregar_alumno.html"
    context = {
        "titulo":"Registar alumno",
        "form":form
    }
    return render(request, template, context)
