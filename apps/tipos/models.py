from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class TipoMaestro(models.Model):
	nombre = models.CharField(
		max_length=1000,
		null=False,
		blank=False
	)
	prioridad = models.PositiveIntegerField(
		null=False,
		blank=False
	)
	in_main = models.BooleanField(
		verbose_name='En Main',
		null=False,
		blank=False,
		default=False
	)
	def __str__(self):
		return self.nombre
	class Meta:
		verbose_name = _('Tipo Maestro')
		verbose_name_plural = _('Tipos Maestros')

class Tipo(models.Model):
	tipomaestro = models.ForeignKey('tipos.TipoMaestro', on_delete=models.CASCADE)
	nombre = models.CharField(
		max_length=1000,
		null=False,
		blank=False
	)
	prioridad = models.PositiveIntegerField(
		null=False,
		blank=False
	)
	def __str__(self):
		return self.nombre
	class Meta:
		verbose_name = _('Tipo')
		verbose_name_plural = _('Tipos')