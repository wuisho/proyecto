from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
from django.utils.text import slugify

class Alumnos(models.Model):
    Matricula = models.CharField(max_length=200, blank=False)
    Nombre = models.CharField(max_length=200, blank=False)
    Escuela = models.CharField(max_length=200, blank=False)
    Curso = models.CharField(max_length= 200, blank=True, default='programacion')
    Calificacion = models.DecimalField(max_digits=5, decimal_places=2)
    slug  = models.SlugField(blank=True)

    def __unicode__(self):
        return self.Nombre

def alumnos_pre_save_reciever(sender, instance, *args, **kwargs):
    print sender
    print instance
    if not instance.slug:
      instance.slug = slugify(instance.Matricula)

pre_save.connect(alumnos_pre_save_reciever,sender=Alumnos)
