from django.http import HttpResponse
from django.shortcuts import render 

def familiares(request):
    context = {
        'nombre' : 'Maria',
        'Apellido': 'Benegas',
        }
    return render(request, 'index.html', context = context)