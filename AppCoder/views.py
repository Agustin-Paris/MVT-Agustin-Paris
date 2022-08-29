from http.client import HTTPResponse
from typing import TextIO
from django.shortcuts import render
from .models import Familia
from django.http import HttpResponse


def Familiares(request):
    hijo = Familia(nombre="Agustin" ,edad=21, nacimiento="2001-02-26")
    padre = Familia(nombre="Tomas" ,edad=50, nacimiento="1972-02-26")
    madre = Familia(nombre="Maria" ,edad=49, nacimiento="1973-02-26")
    hijo.save()
    padre.save()
    madre.save()
     
     
    texto=f"Nombre de la Madre :{madre.nombre}, edad {madre.edad} años, nacimiento {madre.nacimiento}.<br>Nombre del Padre :{padre.nombre}, edad {padre.edad} años, nacimiento {padre.nacimiento}. <br>  Nombre del Hijo :{hijo.nombre}, edad {hijo.edad} años, nacimiento {hijo.nacimiento}."

    return HttpResponse(texto)








""""   
    texto=f"Nombre de la Madre :{madre.nombre}, edad {madre.edad}, nacimiento {madre.nacimiento}"
    texto1=f"Nombre del Padre :{padre.nombre}, edad {padre.edad}, nacimiento {padre.nacimiento}"
    texto2=f" Nombre del Hijo :{hijo.nombre}, edad {hijo.edad}, nacimiento {hijo.nacimiento}"""