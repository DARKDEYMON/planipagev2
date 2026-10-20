from django.shortcuts import render
from apps.users.generic import *
from django.db.models import Count, Q
from django.apps import apps
from apps.publicaciones.views import (
	UpdatePublicacionView,
	CreatePublicacionView,
	archivo_form_inline_view
)
from django.urls import reverse_lazy
from .forms import *
# Create your views here.

class ControlMaestrosListView(ListSearchView):
	model = apps.get_model('tipos', 'TipoMaestro')
	ordering = ['-id']
	paginate_by = 10
	template_name = "controlm/publicacion_controlm.html"
	fields_search = ['id', 'nombre']
	def get_queryset(self):
		return super().get_queryset().filter(user=self.request.user)

class ControlTipoListView(ListSearchView):
	model = apps.get_model('tipos', 'Tipo')
	ordering = ['-id']
	paginate_by = 10
	template_name = "controltipo/controltipo_tipo.html"
	fields_search = ['id', 'nombre']
	def get_queryset(self):
		return super().get_queryset().annotate(
			total_p=Count('publicacion', filter=Q(publicacion__estado='p')),
			total_np=Count('publicacion', filter=~Q(publicacion__estado='p'))
		).filter(
			tipomaestro__id=self.kwargs['pk'] , 
			tipomaestro__user=self.request.user,
		)

class ControlPublicacionListView(ListSearchView):
	model =  apps.get_model('publicaciones', 'Publicacion')
	ordering = ['-id']
	paginate_by = 10
	template_name = "controlp/controlp_list.html"
	fields_search = ['id', 'titulo', 'resumen']
	def get_queryset(self):
		return super().get_queryset().filter(
			tipo__id=self.kwargs['pk'] , 
			tipo__tipomaestro__user=self.request.user,
		)

class ControlUpdatePublicacionView(UpdatePublicacionView):
	success_url = 'controlm:control_archivos_inline'
	form_class  = PublicacionForm
	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		kwargs['user'] = self.request.user
		return kwargs
	def get_object(self, query=None):
		return self.model.objects.get(id=self.kwargs['pk'], tipo__tipomaestro__user=self.request.user)

class ControlCreatePublicacionView(CreatePublicacionView):
	success_url = 'controlm:control_archivos_inline'
	form_class = PublicacionForm
	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		kwargs['user'] = self.request.user
		return kwargs

def control_archivo_form_inline_view(request, *args, **kwargs):
	res = apps.get_model('publicaciones','Publicacion').objects.get(id=kwargs['pk'], tipo__tipomaestro__user=request.user)
	kwargs['success_url'] = reverse_lazy('controlm:controlpublicacion_list', kwargs={'pk':res.tipo.all()[0].pk})
	return archivo_form_inline_view(request, *args, **kwargs)
