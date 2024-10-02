from django import forms
from .models import *

class MaestroForm(forms.ModelForm ):
    class Meta:
        model = TipoMaestro
        exclude = ['']
class TipoForm(forms.ModelForm ):
    class Meta:
        model = Tipo
        exclude = ['']