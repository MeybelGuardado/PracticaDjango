from django.shortcuts import render, redirect
from .models import Curso, Estudiante
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, "base.html")

#Gestión
def gestionarEstudiantes(request):
    estudiantesListados = Estudiante.objects.all()
    return render(request, "gestionEstudiantes.html", {"estudiantes": estudiantesListados})

def gestionarCursos(request):
    cursosListados = Curso.objects.all()
    return render(request, "gestionCursos.html", {"cursos": cursosListados})

#Registro
def registrarCurso(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    creditos=request.POST['numCredito']

    curso=Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)
    return redirect('/gestionarCursos/')

def registrarEstudiante(request):
    carnet=request.POST['txtCarnet']
    nombres=request.POST['txtNombres']
    apellidos=request.POST['txtApellidos']
    edad=request.POST['numEdad']

    estudiante=Estudiante.objects.create(carnet=carnet, nombres=nombres, apellidos=apellidos, edad=edad)
    return redirect('/gestionarEstudiantes/')

#Edición
def edicionCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, "edicionCurso.html", {"curso": curso})

def edicionEstudiante(request, carnet):
    estudiante = Estudiante.objects.get(carnet=carnet)
    return render(request, "edicionEstudiante.html", {"estudiante": estudiante})

#Editar datos
def editarCurso(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    creditos=request.POST['numCredito']

    curso=Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()

    return redirect('/gestionarCursos/')

def editarEstudiante(request):
    carnet=request.POST['txtCarnet']
    nombres=request.POST['txtNombres']
    apellidos=request.POST['txtApellidos']
    edad=request.POST['numEdad']

    estudiante=Estudiante.objects.get(carnet=carnet)
    estudiante.nombres = nombres
    estudiante.apellidos = apellidos
    estudiante.edad = edad
    estudiante.save()

    return redirect('/gestionarEstudiantes/')

#Eliminación
def eliminarCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()

    return redirect('/gestionarCursos/')

def eliminarEstudiante(request, carnet):
    estudiante = Estudiante.objects.get(carnet=carnet)
    estudiante.delete()

    return redirect('/gestionarEstudiantes/')