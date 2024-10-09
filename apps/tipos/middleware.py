from .models import *

class TiposMaestrosMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response
	def __call__(self, request):
		request.tipo_maestro = TipoMaestro.objects.all().prefetch_related('tipo_set')
		response = self.get_response(request)
		return response
