from django.urls import path

from .views import registro,iniciar, menu, salir, verperfil

urlpatterns = [
    path('registro/',registro, name='registro'),
    path('',iniciar,name="iniciar"),
    path('menu/', menu, name='menu'),
    path('salir/', salir, name='salir'),
    path('verperfil/', verperfil, name='verperfil'),
   
]