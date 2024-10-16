from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import Prefetch, Q

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
	def fotos(self):
		return self.archivo_set.filter(
			Q(archivo__iendswith='.jpg')|
			Q(archivo__iendswith='.png')|
			Q(archivo__iendswith='.webp')|
			Q(archivo__iendswith='.svg')
		)
	def archibos(self):
		return self.archivo_set.filter(
			~Q(archivo__iendswith='.jpg')|
			~Q(archivo__iendswith='.png')|
			~Q(archivo__iendswith='.webp')|
			~Q(archivo__iendswith='.svg')
		)
	def __str__(self):
		return self.titulo
	class Meta:
		verbose_name = _('Publicacion')
		verbose_name_plural = _('Publicaciones')

class Archivo(models.Model):
	publicacion = models.ForeignKey('publicaciones.Publicacion', on_delete=models.CASCADE)
	archivo = models.FileField(upload_to='archivos/%Y-%m-%d-%H-%M-%S/')
	prioridad = models.PositiveIntegerField(
		null=False,
		blank=False,
		default=1
	)
	class Meta:
		verbose_name = _('Archivo')
		verbose_name_plural = _('Archivos')
	def __str__(self):
		return str(self.publicacion)
