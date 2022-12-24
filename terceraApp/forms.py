from django import forms
from terceraApp.models import Consola

class FormConsola(forms.ModelForm):
    class Meta:
        model = Consola 
        fields = '__all__'

    modelo = forms.CharField()
    marca = forms.CharField()
    capacidad = forms.CharField()
    peso = forms.CharField()
    garantia = forms.CharField()

    modelo.widget.attrs['class'] = 'form-control'
    marca.widget.attrs['class'] = 'form-control'
    capacidad.widget.attrs['class'] = 'form-control'
    peso.widget.attrs['class'] = 'form-control'
    garantia.widget.attrs['class'] = 'form-control'