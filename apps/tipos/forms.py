from django import forms
from .models import *

class TipoMaestroForm(forms.ModelForm):
    class Meta:
        model = TipoMaestro
        exclude = ['']

class TipoForm(forms.ModelForm):
    class Meta:
        model = Tipo
        exclude = ['tipomaestro']
