from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, FormView, DeleteView, DetailView
from apps.users.generic import *
from django.urls import reverse_lazy
from .forms import *

# Create your views here.
class ListPublicacionViews(ListSearchView):
    model = Publicacion
    ordering = ['-id']
    paginate_by = 10
    template_name = "publicacion/publicacion_list.html"
    fields_search = ['id', 'nombre']
	
class CreatePublicacionView(CreateView, FormPageRedirectView):
    form_class = PublicacionForm
    template_name = "publicacion/publicacion_create.html"
    success_url = reverse_lazy('publicaciones:publicacion_list') 
    location = 'tipo_id'

class UpdatePublicacionView(UpdateView, FormPageRedirectView):
    model = Publicacion
    form_class = PublicacionForm
    template_name = "publicacion/publicacion_update.html"
    success_url = reverse_lazy('publicaciones:publicacion_list') 
    location = 'tipo_id'
class DeletePublicacionView(DeleteView):
    model = Publicacion
    template_name = "publicacion/publicacion_delete.html"
    success_url = reverse_lazy('publicaciones:publicacion_list') 
    location = 'tipo_id'

def main(request):
    return render(request, 'main.html', {})
