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
	# verificacion
	"""
	def clean_tipo(self):
		elegidos = self.cleaned_data['tipo']
		if not self.instance.pk:
			return elegidos
		ajenos = self.instance.tipo.exclude(pk__in=self.fields['tipo'].queryset)
		ids = [t.pk for t in elegidos] + [t.pk for t in ajenos]
		return Tipo.objects.filter(pk__in=ids)
	"""
	def _save_m2m(self):
		if (not self.instance.pk or not self.user or self.user.is_superuser or self.user.is_staff):
			return super()._save_m2m()

		# Tipos que el usuario puede gestionar.
		tipos_permitidos = self.fields['tipo'].queryset

		# Tipos ya asignados que no puede gestionar.
		tipos_protegidos = self.instance.tipo.exclude(
		    pk__in=tipos_permitidos.values_list('pk', flat=True)
		)

		# Guardar los campos ManyToMany normalmente.
		super()._save_m2m()

		# Restaurar las asignaciones protegidas.
		self.instance.tipo.add(*tipos_protegidos)
