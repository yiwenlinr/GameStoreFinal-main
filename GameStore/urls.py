from django.contrib import admin
from django.urls import path, include
from primeraApp import views as app1
from segundaApp import views as app2
from terceraApp import views as app3
from primeraApp.api.router import router_videojuegos
from segundaApp.api.router import router_empleados
from terceraApp.api.router import router_Consola

urlpatterns = [
    path('admin/', admin.site.urls),
    path('videojuegos/api/', include(router_videojuegos.urls)),
    path('', app1.index),
    ## Paths de videojuegos
    path('videojuegos', app1.listadoVideojuegos),
    path('insertarVideojuegos', app1.insertarVideojuegos),
    path('eliminarVideojuegos/<int:id>', app1.eliminarVideojuegos),
    path('modificarVideojuegos/<int:id>', app1.modificarVideojuegos),
    
    ## Paths de empleados
    path('empleados/api/', include(router_empleados.urls)),
    path('empleados', app2.listadoEmpleados),
    path('insertarEmpleados', app2.insertarEmpleados),
    path('eliminarEmpleados/<int:id>', app2.eliminarEmpleados),
    path('modificarEmpleados/<int:id>', app2.modificarEmpleados),
    ## Paths de consolas
    path('consolas/api/', include(router_Consola.urls)),
    path('consolas', app3.listadoConsolas),
    path('insertarConsolas', app3.insertarConsolas),
    path('eliminarConsolas/<int:id>', app3.eliminarConsolas),
    path('modificarEmpleados/<int:id>', app3.modificarConsolas)
]

