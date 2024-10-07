from django import forms
from django.forms.models import inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, HTML
from crispy_bootstrap5.bootstrap5 import FloatingField
from apps.users.generic import Html5DateInput
from .models import *

class PublicacionForm(forms.ModelForm):
	class Meta:
		model = Publicacion
		exclude = ['']

class ArchivoForm(forms.ModelForm):
	class Meta:
		model = Archivo
		exclude = ['publicacion']

class ArchivoFormserHelerForm(FormHelper):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.form_method = 'post'
		self.layout = Layout(
			Row(
				Column('archivo'),
				Column('prioridad'),
				Column('DELETE', css_class="d-flex align-items-center pt-3"),
				css_class='g-1',
			),
			HTML('<hr class="border border-primary border-3 opacity-75">')
		)
		self.render_required_fields = True
		self.form_tag = False

archivo_form_inline = inlineformset_factory(Publicacion, Archivo, form=ArchivoForm, extra=1, can_delete=True)
