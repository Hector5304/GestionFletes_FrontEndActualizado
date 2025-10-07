from django import forms
from .models import Conductores

class ConductoresForm(forms.ModelForm):
    rut = forms.CharField(error_messages={'unique':'Ya existe un conductor con este RUT.'})
    licencia = forms.CharField(error_messages={'unique':'Ya existe un conductor con esta LICENCIA.'})
    class Meta:
        model = Conductores
        fields = ['rut','nombre','apellido','fechaNacimiento','direccion','licencia']
