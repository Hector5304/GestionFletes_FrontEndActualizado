from django import forms
from .models import Ingresos, Egresos

class IngresosForm(forms.ModelForm):
    class Meta:
        model = Ingresos
        fields = ['valor', 'fecha', 'recorrido', 'comentario']

    def __init__(self, *args, **kwargs):
        super(IngresosForm, self).__init__(*args, **kwargs)
        
        self.fields['comentario'].required = False

class EgresosForm(forms.ModelForm):
    class Meta:
        model = Egresos
        fields = ['valor', 'fecha', 'recorrido', 'comentario']
    
    def __init__(self, *args, **kwargs):
        super(EgresosForm, self).__init__(*args, **kwargs)
        
        self.fields['comentario'].required = False