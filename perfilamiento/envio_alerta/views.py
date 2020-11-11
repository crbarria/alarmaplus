from django.shortcuts import render

# Create your views here.

def envio(request):
    return render(
        request,
        'usuario/alerta.html'
    )

def activarAlerta(request):
    return render(
        request,
        'usuario/activarAlerta.html'
    )