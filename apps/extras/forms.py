from django import forms
from .models import *

class PaginaForm(forms.ModelForm):
	class Meta:
		model = Pagina
		exclude = ['']
class MiembroForm(forms.ModelForm):
    class Meta:
        model = Miembro
        fields = ['nombre', 'apellidop', 'apellidom', 'cargo', 'prioridad']
