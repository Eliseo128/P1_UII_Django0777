# from django.http import HttpResponse
from django.shortcuts import render

def paginainicio(request):
    # return HttpResponse('Hola clase del alumno 0777 soy la vista inicial')
    return render(request, 'inicio.html')
def acercade(request):
    # return HttpResponse('Mi pagina acerca de....')
    return render(request, 'acercade.html')