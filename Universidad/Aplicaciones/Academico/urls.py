from django.urls import path
from . import views

urlpatterns = [
    path('', views.home), #Directorio raiz
    path('registrarCurso/', views.registrarCurso),
    path('edicionCurso/<codigo>', views.edicionCurso),
    path('editarCurso/', views.editarCurso),
    path('eliminarCurso/<codigo>', views.eliminarCurso)
]
