from django.db import models

class Conductores(models.Model):
    conductorID = models.AutoField(primary_key=True)
    rut = models.CharField(unique= True, max_length=10)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fechaNacimiento = models.DateField()
    direccion = models.CharField(max_length=100)
    licencia = models.CharField(unique=True, max_length=10)

    def __str__(self):
        texto= "{0} {1} {2} {3} {4} {5} {6}"
        return texto.format(self.conductorID, self.rut, self.nombre, self.apellido, self.fechaNacimiento, self.direccion, self.licencia)
