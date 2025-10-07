from django import forms
from .models import Conductores
from utils.rut_validator import validar_rut, formatear_rut


class ConductoresForm(forms.ModelForm):
    rut = forms.CharField(
        error_messages={'unique': 'Ya existe un conductor con este RUT.'},
        help_text='Formato: 12.345.678-9 o 12345678-9',
        widget=forms.TextInput(attrs={
            'placeholder': '12.345.678-9',
            'class': 'form-control'
        })
    )
    licencia = forms.CharField(
        error_messages={'unique': 'Ya existe un conductor con esta LICENCIA.'},
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = Conductores
        fields = ['rut', 'nombre', 'apellido', 'fechaNacimiento', 'direccion', 'licencia']
    
    def clean_rut(self):
        """Valida y formatea el RUT ingresado"""
        rut = self.cleaned_data.get('rut')
        
        if not rut:
            raise forms.ValidationError('El RUT es obligatorio.')
        
        # Validar formato y dígito verificador
        if not validar_rut(rut):
            raise forms.ValidationError(
                'RUT inválido. Verifique el número y el dígito verificador.'
            )
        
        # Formatear el RUT de manera consistente (sin puntos, con guion)
        rut_limpio = rut.replace(".", "").replace("-", "").replace(" ", "")
        if len(rut_limpio) >= 2:
            rut_formateado = f"{rut_limpio[:-1]}-{rut_limpio[-1].upper()}"
            return rut_formateado
        
        return rut
