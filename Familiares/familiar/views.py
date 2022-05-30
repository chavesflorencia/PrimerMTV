from django.shortcuts import render
from familiar.models import Familiares
# Create your views here.
def family(request):
    familiar_nuevo = Familiares.objects.create(
    name = 'Maria', 
    apellido = 'Benegas', 
    edad = 54, 
    dni = 20242660, 
    fecha_cumpleanios = 13/8/1968)
    context= {'familiar_nuevo':familiar_nuevo}
    return render (request, 'familiar1.html', context=context)