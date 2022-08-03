from django.db import models
from django.shortcuts import render

# Create your models here.

class Curso(models.Model):

    nombre = models.CharField(max_length=50)
    camada = models.IntegerField()

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    documento = models.IntegerField()
    fecha = models.DateField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)

class Entregable(models.Model):
    nombre = models.CharField(max_length=50)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()