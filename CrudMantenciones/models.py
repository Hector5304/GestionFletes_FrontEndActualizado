from django.db import models
from CrudVehiculos.models import Vehiculos

class Mantenciones(models.Model):
    mantencionID = models.AutoField(primary_key=True)
    vehiculo = models.ForeignKey(Vehiculos, on_delete=models.CASCADE)
    fechaInicio = models.DateField()
    duracion = models.PositiveIntegerField()
    valor = models.PositiveIntegerField()

    def __str__(self):
        texto= "{0} {1} {2} {3} {4}"
        return texto.format(self.mantencionID, self.vehiculo, self.fechaInicio, self.duracion, self.valor)
