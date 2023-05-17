from django.urls import path
from . import views

urlpatterns = [
    path('', views.home), #Directorio raiz
    path('gestionarEstudiantes/', views.gestionarEstudiantes),
    path('gestionarCursos/', views.gestionarCursos),
    path('registrarCurso/', views.registrarCurso),
    path('registrarEstudiante/', views.registrarEstudiante),
    path('edicionCurso/<codigo>', views.edicionCurso),
    path('edicionEstudiante/<carnet>', views.edicionEstudiante),
    path('editarCurso/', views.editarCurso),
    path('editarEstudiante/', views.editarEstudiante),
    path('eliminarCurso/<codigo>', views.eliminarCurso),
    path('eliminarEstudiante/<carnet>', views.eliminarEstudiante)
]
