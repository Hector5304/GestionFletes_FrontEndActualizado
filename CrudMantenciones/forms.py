from django import forms
from .models import Mantenciones
from datetime import date

class MantencionForm(forms.ModelForm):
    class Meta:
        model = Mantenciones
        fields = ['vehiculo','fechaInicio','duracion','valor']
    
    def __init__(self, *args, **kwargs):
        super(MantencionForm, self).__init__(*args, **kwargs)
        self.fields['fechaInicio'].widget.attrs['max'] = str(date.today())