from django.db import models
from CrudConductores.models import Conductores
from CrudVehiculos.models import Vehiculos

class Recorridos(models.Model):
    recorridoID = models.AutoField(primary_key=True)
    conductor = models.ForeignKey(Conductores, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculos, on_delete=models.CASCADE)
    fecha = models.DateField()
    direccionOrigen = models.CharField(max_length=50)
    direccionDestino = models.CharField(max_length=50)
    carga = models.TextField(max_length=100)
    detalle = models.TextField(max_length=100, null=True)
    distancia_km = models.FloatField(null=True, blank=True, help_text='Distancia recorrida en km')
    gps_data = models.JSONField(null=True, blank=True, help_text='Datos GPS del recorrido (lista de puntos, GPX, etc)')

    def __str__(self):
        texto= "{0} {1} {2} {3} {4} {5} {6} {7}"
        return texto.format(self.recorridoID, self.conductor, self.vehiculo, self.fecha, self.direccionOrigen, self.direccionDestino, self.carga, self.detalle)
