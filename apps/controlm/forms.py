from django import forms
from django.apps import apps

class PublicacionForm(forms.ModelForm):
	class Meta:
		model = apps.get_model('publicaciones','Publicacion')
		exclude = ['']
	def __init__(self, *args, **kwargs):
		user = kwargs.pop('user', None)
		super().__init__(*args, **kwargs)
		self.fields['tipo'].queryset = apps.get_model('tipos','Tipo').objects.filter(tipomaestro__user=user)
