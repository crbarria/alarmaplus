from django.shortcuts import render

# Create your views here.

def envio(request):
    return render(
        request,
        'usuario/alerta.html'
    )