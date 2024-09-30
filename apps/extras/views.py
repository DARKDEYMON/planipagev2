from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, FormView, DeleteView, DetailView
from apps.users.generic import *
from .forms import *

# Create your views here.

class ListPaginaView(ListSearchView):
	model = Pagina
	ordering = ['-id']
	paginate_by = 10
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