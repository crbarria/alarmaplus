from django.urls import path

from .views import registro,iniciar, menu, salir, verperfil, modificar,listar, eliminar

urlpatterns = [
    path('registro/',registro, name='registro'),
    path('',iniciar,name="iniciar"),
    path('menu/', menu, name='menu'),
    path('salir/', salir, name='salir'),
    path('verperfil/', verperfil, name='verperfil'),
    path('modificar/<int:id>', modificar, name='modificar'),
    path('listar/', listar, name='listar'),
    path('eliminar/<int:id>', eliminar, name='eliminar')   
]