from .models import *

class UltimasPublicaionesMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response
	def __call__(self, request):
		request.ultimas_publicaciones = Publicacion.objects.filter(publicado=True).order_by('-id')[:5]
		response = self.get_response(request)
		return response
