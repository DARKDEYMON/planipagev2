from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, FormView, DeleteView, DetailView
from apps.users.generic import *
from .forms import *


# Create your views here.
class ListTipoMaestroView(ListSearchView):
    model = TipoMaestro
    ordering = ['-id']
    paginate_by = 10
    template_name = 'tipomaestro/tipomaestro_list.html'
    fields_search = ['id', 'nombre']

class CreateTipoMaestroView(CreateView, FormPageRedirectView):
    model = TipoMaestro
    form_class = TipoMaestroForm
    template_name = 'tipomaestro/tipomaestro_create.html'
    success_url = reverse_lazy('tipos:maestro_list')

class UpdateTipoMaestroView(UpdateView, FormPageRedirectView):
    model = TipoMaestro
    form_class = TipoMaestroForm
    template_name = 'tipomaestro/tipomaestro_update.html'
    success_url = reverse_lazy('tipos:maestro_list')

class DeleteTipoMaestroView(DeleteView):
    model = TipoMaestro
    template_name = 'tipomaestro/tipomaestro_delete.html'
    success_url = reverse_lazy('tipos:maestro_list')

#tipo
class ListTipoView(ListSearchView, ModelExtraView):
    model_extra = TipoMaestro
    model = Tipo
    ordering = ['-id']
    paginate_by = 10
    template_name = 'tipo/tipo_list.html'
    fields_search = ['id', 'nombre']
    def get_queryset(self):
        query = super().get_queryset()
        return query.filter(tipomaestro=self.kwargs['pk'])

class TipoCreateView(FormPageRedirectView, CreateViewInternal):
    model_extra = TipoMaestro
    form_class = TipoForm
    template_name = 'tipo/tipo_create.html'
    success_url = 'tipos:tipo_list'
    location = 'tipomaestro_id'

class TipoUpdateView(FormPageRedirectView, UpdateViewInternal):
    model = Tipo
    form_class = TipoForm
    template_name = 'tipo/tipo_update.html'
    success_url = 'tipos:tipo_list'
    location = 'tipomaestro_id'

class TipoDeleteView(DeleteViewInternal):
    model = Tipo
    template_name = 'tipo/tipo_delete.html'
    success_url = 'tipos:tipo_list'
    location = 'tipomaestro_id'
