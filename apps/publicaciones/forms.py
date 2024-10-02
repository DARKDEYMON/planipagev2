from django import forms
from .models import *

class PublicacionForm(forms.ModelForm):
	class Meta:
		model = Publicacion
		exclude = ['']