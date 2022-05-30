from django.http import HttpResponse
from django.shortcuts import render 

def familiares(request):
    context = {}
    return render(request, 'index.html', context = context)