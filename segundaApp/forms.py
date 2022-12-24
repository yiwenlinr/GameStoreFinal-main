from django import forms
from segundaApp.models import Empleados

class FormEmpleados(forms.ModelForm):
    class Meta:
        model = Empleados
        fields = '__all__'

    nombre = forms.CharField()
    cargo = forms.CharField()
    email = forms.EmailField()
    telefono = forms.CharField()
    direccion = forms.CharField()
    horario = forms.CharField()

    nombre.widget.attrs['class'] = 'form-control'
    cargo.widget.attrs['class'] = 'form-control'
    email.widget.attrs['class'] = 'form-control'
    telefono.widget.attrs['class'] = 'form-control'
    direccion.widget.attrs['class'] = 'form-control'
    horario.widget.attrs['class'] = 'form-control'