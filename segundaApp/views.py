from django.shortcuts import render
from segundaApp.forms import FormEmpleados
from segundaApp.models import Empleados
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'primeraApp/index.html')

def listadoEmpleados(request):
    empleados = Empleados.objects.all()
    data = {'empleados': empleados}
    return render(request, 'segundaApp/empleados.html', data)

def insertarEmpleados(request):
    form = FormEmpleados()
    if request.method == 'POST':
        form = FormEmpleados(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
    data = {'form': form}
    return render(request, 'segundaApp/insertarEmpleado.html', data)

def eliminarEmpleados(request, id):
    empleados = Empleados.objects.get(id = id)
    empleados.delete()
    return HttpResponseRedirect('/empleados')

def modificarEmpleados(request, id):
    empleados = Empleados.objects.get(id = id)
    form = FormEmpleados(instance=empleados)
    if request.method == 'POST':
        form = FormEmpleados(request.POST, instance=empleados)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'segundaApp/insertarEmpleado.html', data)