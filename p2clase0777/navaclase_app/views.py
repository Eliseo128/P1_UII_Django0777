from django.shortcuts import render
from django.http import HttpResponse

def hola(request):
    return  render(request,'navaclase_app/index.html')

def cbtis(request):
    return HttpResponse('Hola jaguares grupo 5 I,J jaja')

def alumnos(request,nombre): # minuto 50:12 la moneda
    return HttpResponse(f'{nombre} !!!! estas en el grupo machin')

# https://youtu.be/vXR5CAcRv5w?si=pz273pPKda4YLG16