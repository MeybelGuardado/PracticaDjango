from django.shortcuts import render, redirect
from .models import Curso
from django.contrib import messages

# Create your views here.

def home(request):
    cursosListados = Curso.objects.all() #Retorna el listado de todos los cursos
    return render(request, "gestionCursos.html", {"cursos": cursosListados})

def registrarCurso(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    creditos=request.POST['numCredito']

    curso=Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)
    return redirect('/')

def edicionCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, "edicionCurso.html", {"curso": curso})

def editarCurso(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    creditos=request.POST['numCredito']

    curso=Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()

    return redirect('/')

def eliminarCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()

    return redirect('/')
