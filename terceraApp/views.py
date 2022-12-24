from django.shortcuts import render
from terceraApp.forms import FormConsola
from terceraApp.models import Consola
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'primeraApp/index.html')

def listadoConsolas(request):
    consolas = Consola.objects.all()
    data = {'consolas': consolas}
    return render(request, 'terceraApp/consolas.html', data)

def insertarConsolas(request):
    form = FormConsola()
    if request.method == 'POST':
        form = FormConsola(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
    data = {'form': form}
    return render(request, 'terceraApp/insertarConsolas.html', data)

def eliminarConsolas(request, id):
    consolas = Consola.objects.get(id = id)
    consolas.delete()
    return HttpResponseRedirect('/consolas')

def modificarConsolas(request, id):
    consolas = Consola.objects.get(id = id)
    form = FormConsola(instance=consolas)
    if request.method == 'POST':
        form = FormConsola(request.POST, instance=consolas)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'terceraApp/insertarConsolas.html', data)


