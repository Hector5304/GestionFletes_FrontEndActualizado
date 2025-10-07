from django.db import models


class Vehiculos(models.Model):
    vehiculoID = models.AutoField(primary_key=True)
    patente = models.CharField(max_length=6, unique=True)
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=50)
    fechaAdquisicion = models.DateField()
    estado = models.CharField(max_length=10, choices=[('activo', 'Activo'),('inactivo', 'Inactivo'),], default='inactivo')
    comentario = models.TextField(max_length=200, blank=True, null=True)

    # Nuevo: tipo de bencina y rendimiento
    TIPO_BENCINA_CHOICES = [
        ('93', '93'),
        ('95', '95'),
        ('97', '97'),
        ('diesel', 'Diésel'),
    ]
    tipo_bencina = models.CharField(max_length=10, choices=TIPO_BENCINA_CHOICES, default='93')
    rendimiento = models.FloatField(help_text='Km por litro', default=10)

    def __str__(self):
        texto= "{0} {1} {2} {3} {4} {5} {6}"
        return texto.format(self.vehiculoID, self.patente, self.marca, self.modelo, self.fechaAdquisicion, self.estado, self.comentario)