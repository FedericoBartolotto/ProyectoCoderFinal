
from django.urls import path
from App_coder.views import Inicio, Estudiante, Curso, Entregable, Profesor

urlpatterns = [
    path('Inicio/', inicio),
    path('Estudiante/', Estudiante),
    path('Curso/', Curso),
    path('Entregable', Entregable),
    path('Profesor/', Profesor),
    ]
