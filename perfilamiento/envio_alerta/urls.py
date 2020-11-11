from django.urls import path

from .views import envio, activarAlerta

urlpatterns = [
     path('envio/',envio, name='envio'),
     path('activarAlerta/',activarAlerta, name='activarAlerta')
]
