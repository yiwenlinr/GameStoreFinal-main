from django import forms
from primeraApp.models import Videojuegos

class FormVideojuegos(forms.ModelForm):
    class Meta:
        model = Videojuegos
        fields = '__all__'

    nombre = forms.CharField()
    desarrollador = forms.CharField()
    generos = forms.CharField()
    plataformas = forms.CharField()
    fecha_lanzamiento = forms.DateField()
    puntuacion = forms.CharField()

    nombre.widget.attrs['class'] = 'form-control'
    desarrollador.widget.attrs['class'] = 'form-control'
    generos.widget.attrs['class'] = 'form-control'
    plataformas.widget.attrs['class'] = 'form-control'
    fecha_lanzamiento.widget.attrs['class'] = 'form-control'
    puntuacion.widget.attrs['class'] = 'form-control'