from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('perfil.urls')),
    path('',include('envio_alerta.urls'))
]
