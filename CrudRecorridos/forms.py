from django import forms
from .models import Recorridos
from CrudConductores.models import Conductores

class RecorridosForm(forms.ModelForm):
    class Meta:
        model = Recorridos
        fields = ['conductor','vehiculo','fecha','direccionOrigen','direccionDestino','carga','detalle','distancia_km','gps_data']