from django.shortcuts import render, redirect
from primeraApp.forms import FormVideojuegos
from primeraApp.models import Videojuegos
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'primeraApp/index.html')

def listadoVideojuegos(request):
    videojuegos = Videojuegos.objects.all()
    data = {'videojuegos': videojuegos}
    return render(request, 'primeraApp/videojuegos.html', data)

def insertarVideojuegos(request):
    form = FormVideojuegos()
    if request.method == 'POST':
        form = FormVideojuegos(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
    data = {'form': form}
    return render(request, 'primeraApp/insertarVideojuego.html', data)

def eliminarVideojuegos(request, id):
    videojuegos = Videojuegos.objects.get(id = id)
    videojuegos.delete()
    return redirect('/videojuegos')

def modificarVideojuegos(request, id):
    videojuegos = Videojuegos.objects.get(id = id)
    form = FormVideojuegos(instance=videojuegos)
    if request.method == 'POST':
        form = FormVideojuegos(request.POST, instance=videojuegos)
        if form.is_valid():
            form.save()
        return index(request) 
    data = {'form': form}
    return render(request, 'primeraApp/insertarVideojuego.html', data)
