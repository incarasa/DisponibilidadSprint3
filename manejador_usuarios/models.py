from django.db import models

class Estudiante(models.Model):
    nombre =  models.CharField(max_length=50)
    curso = models.CharField(max_length=15)
    edad = models.IntegerField()

    def __str__(self) -> str:
        return str(self.nombre)
    
class Pago(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    valor = models.IntegerField()
    fecha = models.CharField(max_length=50)

    def __str__(self) -> str:
        return str(self.id)
