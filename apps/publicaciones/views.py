from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, FormView, DeleteView, DetailView
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.http import HttpResponseRedirect
from apps.users.generic import *
from django.urls import reverse_lazy
from django.apps import apps
from django.db.models import Prefetch, Q
from .forms import *

# Create your views here.
class ListPublicacionViews(ListSearchView):
    model = Publicacion
    ordering = ['-id']
    paginate_by = 10
    template_name = "publicacion/publicacion_list.html"
    fields_search = ['id', 'titulo', 'resumen']
	
class CreatePublicacionView(CreateView, FormPageRedirectView):
    form_class = PublicacionForm
    template_name = "publicacion/publicacion_create.html"
    success_url = 'publicaciones:publicaciones_inline'
    location = 'tipo_id'
    def get_success_url(self):
        return reverse_lazy(self.success_url, kwargs={'pk':self.object.id})

class UpdatePublicacionView(UpdateView, FormPageRedirectView):
    model = Publicacion
    form_class = PublicacionForm
    template_name = "publicacion/publicacion_update.html"
    success_url = 'publicaciones:publicaciones_inline'
    location = 'tipo_id'
    def get_success_url(self):
        return reverse_lazy(self.success_url, kwargs={'pk':self.object.id})

class DeletePublicacionView(DeleteView):
    model = Publicacion
    template_name = "publicacion/publicacion_delete.html"
    success_url = reverse_lazy('publicaciones:publicacion_list') 
    location = 'tipo_id'

def archivo_form_inline_view(request, pk):
    instance =  get_object_or_404(Publicacion, id=pk)
    form_inline = archivo_form_inline
    extra_field = form_inline().empty_form
    helper = ArchivoFormserHelerForm()
    if request.POST:
        formset = form_inline(request.POST, request.FILES, instance=instance)
        if formset.is_valid():
            formset.save()
            if('guardar-volver' in request.POST):
                return HttpResponseRedirect(reverse_lazy('publicaciones:publicacion_list')+'?idpage=' + str(pk))
            return HttpResponseRedirect(request.path)
    else:
        formset = form_inline(instance=instance)
    return render(request, 'archivo/archivo_inline.html', {'formset':formset, 'instance':instance, 'extra_field': extra_field, 'helper':helper})

def main(request):
    carousel = Publicacion.objects.filter(publicado=True).prefetch_related(
        Prefetch('archivo_set', Archivo.objects.filter(
                Q(archivo__iendswith='.jpg')|
                Q(archivo__iendswith='.png')|
                Q(archivo__iendswith='.webp')|
                Q(archivo__iendswith='.svg')
            ).order_by('id')
        )
    ).order_by('-id')[:5]
    in_main = apps.get_model('tipos', 'Tipo').objects.prefetch_related('publicacion_set').select_related('tipomaestro').filter(
        in_main=True,
        publicacion__isnull=False
    )
    return render(request, 'main.html', {'carousel':carousel, 'in_main':in_main})

#vista de render
class ListVistaPublicaionesView(ListSearchView):
    model = Publicacion
    paginate_by = 9
    template_name = 'publicacion/list_vistapublicacion.html'
    def get_queryset(self):
        return super().get_queryset().filter(publicado=True).prefetch_related(
            'tipo', 
            Prefetch('archivo_set', Archivo.objects.filter(
                    Q(archivo__iendswith='.jpg')|
                    Q(archivo__iendswith='.png')|
                    Q(archivo__iendswith='.webp')|
                    Q(archivo__iendswith='.svg')
                )
            )
        ).filter(tipo__id=self.kwargs['pk'])
