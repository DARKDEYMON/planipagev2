from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, FormView, DeleteView, DetailView
from .forms import *

# Create your views here.

class ListPaginaView(ListView):
	model = Pagina
	ordering = ['-id']
	paginate_by = 10
	template_name = 'pagina/pagina_list.html'
