from django import forms
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from constance import config
from django.conf import settings
from .models import *

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
			'ci'
		]
	def __init__(self, *args, **kwargs):
		super(CreateUserForm, self).__init__(*args, **kwargs)
		self.fields['email'].required = True
		self.fields['first_name'].required = True
		self.fields['last_name'].required = True
		self.fields['ci'].required = True

class AddPermissionsForm(forms.Form):
	def __init__(self, *args, **kwargs):
		#esto permite aderir datos al constructor dinamicamente deste arg y kwargs
		model_permissions = kwargs.pop('model_permissions', None)
		showd_permissions = kwargs.pop('showd_permissions', False)
		super(AddPermissionsForm, self).__init__(*args, **kwargs)

		content_type = ContentType.objects.get_for_model(model_permissions)
		permission = Permission.objects.filter(content_type=content_type).order_by('id')
		for idx, p in enumerate(permission):
			if(showd_permissions):
				self.fields[p.codename] = forms.BooleanField(label='Dar permiso para el modulo: '+ str(p.name), required=False)
			else:
				if(idx>3):
					self.fields[p.codename] = forms.BooleanField(label='Dar permiso para el modulo: '+ str(p.name), required=False)

class ConstanceForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for key in self.Meta.constance_values.keys():
			data = self.Meta.constance_values[key]
			typo = self.getDataOrNone(data,2)
			if not typo or typo==str:
				self.fields[key] = forms.CharField(label=data[1], required=True, initial=getattr(self.Meta.constance,key))
			elif(typo==bool):
				self.fields[key] = forms.BooleanField(label=data[1], required=True, initial=getattr(self.Meta.constance,key))
			elif(typo==int):
				self.fields[key] = forms.IntegerField(label=data[1], required=True, initial=getattr(self.Meta.constance,key))
			elif(typo==float):
				self.fields[key] = forms.FloatField(label=data[1], required=True, initial=getattr(self.Meta.constance,key))
	
			if(key in self.Meta.widget):
				self.fields[key].widget = self.Meta.widget[key]
	def getDataOrNone(self, data, index):
		try:
			return data[index]
		except Exception as e:
			return None
	def save(self):
		for key in self.cleaned_data:
			setattr(self.Meta.constance, key, self.cleaned_data[key])
	class Meta:
		constance = config
		constance_values = settings.CONSTANCE_CONFIG
		widget = {
			'EXTRAS': forms.Textarea()
		}
