from django.shortcuts import render
from django.http import HttpResponse
from App_coder.models import inicio, Estudiante, Profesor, Curso, Entregable

# Create your views here.

def inicio(self):
    return HttpResponse("Vista inicio")
    
def estudiante(self):
    return HttpResponse("Vista estudiante")

def profesores(self):
    return HttpResponse("Vista profesores")

def curso(self):
    return HttpResponse("Vista curso")

def entregable(self):
    return HttpResponse("Vista entregable")
