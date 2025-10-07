from django.db import models
from CrudRecorridos.models import Recorridos

class Ingresos(models.Model):
    ingresoID = models.AutoField(primary_key=True)
    valor = models.PositiveIntegerField()
    fecha = models.DateField()
    recorrido = models.ForeignKey(Recorridos, on_delete=models.CASCADE, null=True)
    comentario = models.TextField(max_length=50, null=True)
    def __str__(self):
        texto= "{0} {1} {2} {3} {4}"
        return texto.format(self.ingresoID, self.valor, self.fecha, self.recorrido, self.comentario)

class Egresos(models.Model):
    egresoID = models.AutoField(primary_key=True)
    valor = models.PositiveIntegerField()
    fecha = models.DateField()
    recorrido = models.ForeignKey(Recorridos, on_delete=models.CASCADE, null=True)
    comentario = models.TextField(max_length=50, null=True)
    def __str__(self):
        texto= "{0} {1} {2} {3} {4}"
        return texto.format(self.egresoID, self.valor, self.fecha, self.recorrido, self.comentario)