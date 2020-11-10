from django.urls import path

from .views import envio

urlpatterns = [
  
     path('envio/',envio, name='envio')
   
]
