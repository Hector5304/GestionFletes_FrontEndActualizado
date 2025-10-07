from django import forms
from .models import Vehiculos

class VehiculosForm(forms.ModelForm):
    patente = forms.CharField(error_messages={'unique':'La patente ya existe'})
    fechaAdquisicion = forms.DateField(label='Fecha de Adquisicion')
    class Meta:
        model = Vehiculos
        fields = ['patente','marca','modelo','fechaAdquisicion','estado','comentario']

    def clean_patente(self):
        patente = self.cleaned_data.get('patente','').strip()
        import re
        if not patente:
            raise forms.ValidationError('La patente es obligatoria')
        # simple pattern: allow letters/numbers and dashes
        if not re.match(r'^[A-Z0-9-]{4,15}$', patente, re.I):
            raise forms.ValidationError('Formato de patente inválido')
        return patente.upper()

    def clean(self):
        cleaned = super().clean()
        marca = cleaned.get('marca','')
        modelo = cleaned.get('modelo','')
        if not marca:
            self.add_error('marca','La marca es obligatoria')
        if not modelo:
            self.add_error('modelo','El modelo es obligatorio')
        return cleaned