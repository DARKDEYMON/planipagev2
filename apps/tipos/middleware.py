from .models import *
from django.db.models import Prefetch, Q

class TiposMaestrosMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response
	def __call__(self, request):
		request.tipo_maestro = TipoMaestro.objects.all().prefetch_related(
			Prefetch('tipo_set', Tipo.objects.order_by('prioridad','id')),
		).order_by('prioridad','id')
		response = self.get_response(request)
		return response
