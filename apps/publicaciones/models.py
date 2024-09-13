from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Publicacion(models.Model):
	tipo = models.ManyToManyField('tipos.Tipo')
	titulo = models.CharField(
		max_length=1000,
		blank=False,
		null=False
	)
	resumen = models.CharField(
		max_length=2000,
		blank=False,
		null=False
	)
	contenido = models.TextField(
		blank=False,
		null=False
	)
	publicado = models.BooleanField(
		blank=False,
		null=False,
		default=False
	)
	creado = models.DateTimeField(
		blank=False,
		null=False,
		auto_now_add=True
	)
	modificado = models.DateTimeField(
		blank=False,
		null=False,
		auto_now=True
	)
	def __str__(self):
		return self.titulo
	class Meta:
		verbose_name = _('Publicacion')
		verbose_name_plural = _('Publicaciones')