from django import forms
from .models import Alumnos

class AlumnosAddForm(forms.Form):

    Matricula=forms.CharField(label="Cual es su Matricula",
                             widget=forms.TextInput(attrs={'placeholder': 'Introduzca su matricula'}))
    Nombre=forms.CharField(label="Cual es su nombre", widget=forms.TextInput(attrs={'placeholder': 'Introduzca su nombre'}))
    Escuela=forms.CharField(label="Cual es el nombre de la escuela", widget=forms.TextInput(attrs={'placeholder': 'Introduzca el nombre de la escuela'}))
    Curso=forms.CharField(label="Cual es el nombre de la escuela", widget=forms.TextInput(attrs={'placeholder': 'Introduzca el nombre de la escuela'}))
    Calificacion=forms.DecimalField()

    def clean_Calificacion(self):
      Calificacion=self.cleaned_data.get("Calificacion")
      if Calificacion <=0.00:
        raise forms.ValidationError("La calificacion debe ser mayor a 0")
      elif Calificacion >=100.01:
        raise forms.ValidationError("La calificacion debe ser menor a 100")
      else:
        return Calificacion

class AlumnosModelForm(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields =[
            "Matricula",
            "Nombre",
            "Curso",
            "Escuela",
            "Calificacion",
        ]
        labels = {
            "Matricula": "Cual es la matricula",
            "Nombre": "Cual es su nombre",
            "Curso": "Cual es el curso",
            "Escuela":"Cual es la escuela",
            "Calificacion":"Cual es la calificacion",

        }
        widgets = {
            "Matricula": forms.TextInput(attrs={'placeholder': 'Introduzca la matricula'}),
            "Nombre":forms.TextInput(attrs={'placeholder': 'Introduzca el nombre'}),
            "Curso":forms.TextInput(attrs={'placeholder': 'Introduzca el curso'}),
            "Escuela": forms.TextInput(attrs={'placeholder': 'Introduzca la escuela'}),
            "Calificacion":forms.NumberInput(),
        }

    def clean_Calificacion(self):
      Calificacion=self.cleaned_data.get("Calificacion")
      if Calificacion <=0.00:
        raise forms.ValidationError("La calificacion debe ser mayor a 0")
      elif Calificacion >=100.01:
        raise forms.ValidationError("La calificacion debe ser menor a 100")
      else:
        return Calificacion
