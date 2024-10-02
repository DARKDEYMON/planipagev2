from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, FormView, DeleteView, DetailView
from apps.users.generic import *
from .forms import *

# Create your views here.

class ListPaginaView(ListSearchView):
	model = Pagina
	ordering = ['-id']
	paginate_by = 4
	template_name = 'pagina/pagina_list.html'
	fields_search = ['id', 'nombre']

class CreatePaginaView(CreateView, FormPageRedirectView):
	form_class = PaginaForm
	template_name = 'pagina/pagina_create.html'
	success_url = reverse_lazy('extras:list_paginas')
	#success_message = '%(nombre)s se creo correctamente'

class UpdatePaginaView(UpdateView, FormPageRedirectView):
	model = Pagina
	form_class = PaginaForm
	template_name = 'pagina/pagina_update.html'
	success_url = reverse_lazy('extras:list_paginas')

class DeletePaginaView(DeleteView):
	model = Pagina
	template_name = 'pagina/pagina_delete.html'
	success_url = reverse_lazy('extras:list_paginas')

#miembros
class ListMiembroView(ListSearchView):
    model = Miembro
    ordering = ['-prioridad', 'id']
    paginate_by = 4  
    template_name = 'miembro/miembro_list.html'
    fields_search = ['id', 'nombre', 'apellidop', 'apellidom', 'cargo']

class CreateMiembroView(CreateView, FormPageRedirectView):
    form_class = MiembroForm
    template_name = 'miembro/miembro_create.html'
    success_url = reverse_lazy('extras:miembro_list')

class UpdateMiembroView(UpdateView, FormPageRedirectView):
    model = Miembro
    form_class = MiembroForm
    template_name = 'miembro/miembro_update.html'
    success_url = reverse_lazy('extras:miembro_list') 

class DeleteMiembroView(DeleteView):
    model = Miembro
    template_name = 'miembro/miembro_delete.html'
    success_url = reverse_lazy('extras:miembro_list')  