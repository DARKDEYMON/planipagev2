from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, FormView, DeleteView, DetailView
from apps.users.generic import *
from .forms import *


# Create your views here.
class MaestroListView(ListSearchView):
    model = TipoMaestro
    ordering = ['-id']
    paginate_by = 10
    template_name = 'maestro/maestro_list.html'
    fields_search = ['id', 'nombre']

class MaestroCreateView(CreateView, FormPageRedirectView):
    model = TipoMaestro
    form_class = MaestroForm
    template_name = 'maestro/maestro_create.html'
    success_url = reverse_lazy('tipos:maestro_list')

class MaestroUpdateView(UpdateView, FormPageRedirectView):
    model = TipoMaestro
    form_class = MaestroForm
    template_name = 'maestro/maestro_update.html'
    success_url = reverse_lazy('tipos:maestro_list')

class MaestroDeleteView(DeleteView):
    model = TipoMaestro
    template_name = 'maestro/maestro_delete.html'
    success_url = reverse_lazy('tipos:maestro_list')

class TipoListView(ListSearchView):
    model = Tipo
    ordering = ['-id']
    paginate_by = 10
    template_name = 'tipo/tipo_list.html'
    fields_search = ['id', 'nombre']

    def get_queryset(self):
        query = super().get_queryset()
        return query.filter(tipomaestro=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['maestro_pk'] = self.kwargs['pk']
        return context

class TipoCreateView(CreateView, FormPageRedirectView):
    model = Tipo
    form_class = TipoForm
    template_name = 'tipo/tipo_create.html'

    def get_success_url(self):
        return reverse_lazy('tipos:tipo_list', kwargs={'pk': self.kwargs['maestro_pk']})

    def form_valid(self, form):
        form.instance.tipomaestro_id = self.kwargs['maestro_pk']
        return super().form_valid(form)

class TipoUpdateView(UpdateView, FormPageRedirectView):
    model = Tipo
    form_class = TipoForm
    template_name = 'tipo/tipo_update.html'

    def get_success_url(self):
        return reverse_lazy('tipos:tipo_list', kwargs={'pk': self.object.tipomaestro.pk})

class TipoDeleteView(DeleteView):
    model = Tipo
    template_name = 'tipo/tipo_delete.html'

    def get_success_url(self):
        return reverse_lazy('tipos:tipo_list', kwargs={'pk': self.object.tipomaestro.pk})
