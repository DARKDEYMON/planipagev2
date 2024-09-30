from django import forms
from .models import *

class PaginaForm(forms.ModelForm):
	class Meta:
		model = Pagina
		exclude = ['']
