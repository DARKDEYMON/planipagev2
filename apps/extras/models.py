from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Miembro(models.Model):
	nombre = models.CharField(
		max_length=500,
		null=False,
		blank=False
	)
	apellidop = models.CharField(
		verbose_name='Apellido Paterno',
		max_length=500,
		null=False,
		blank=False
	)
	apellidom = models.CharField(
		verbose_name='Apellido Materno',
		max_length=500,
		null=False,
		blank=False
	)
	cargo = models.CharField(
		max_length=500,
		null=False,
		blank=False
	)
	prioridad = models.PositiveIntegerField(
		null=False,
		blank=False
	)
	class Meta:
		verbose_name = _('Miembro')
		verbose_name_plural = _('Miembros')
	def __str__(self):
		return self.nombre + " " + self.apellidop

class Pagina(models.Model):
	nombre = models.CharField(
		max_length=1000,
		null=False,
		blank=False
	)
	url = models.URLField(
		null=False,
		blank=False
	)
	class Meta:
		verbose_name = _('Pagina')
		verbose_name_plural = _('Paginas')
	def __str__(self):
		return self.nombre
