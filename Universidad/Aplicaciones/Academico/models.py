from django.db import models

# Create your models here.

class Curso(models.Model):
    codigo=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=50)
    creditos=models.PositiveSmallIntegerField()
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.creditos)
    
class Estudiante(models.Model):
    carnet=models.CharField(primary_key=True,max_length=7)
    nombres= models.CharField(max_length=25)
    apellidos= models.CharField(max_length=25)
    edad= models.PositiveSmallIntegerField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombres, self.carnet)