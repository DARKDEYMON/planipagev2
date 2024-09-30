from django.views.generic import ListView, CreateView, UpdateView, FormView, DeleteView, DetailView
from django.http import HttpResponseRedirect
from django.contrib.postgres.search import TrigramSimilarity
from django.db.models.functions import Coalesce
from django.db.models import Value
from django.db.models import CharField
from django.db.models.functions import Cast
from operator import attrgetter
from django.urls import reverse_lazy
from django.shortcuts import render
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, HTML
from crispy_bootstrap5.bootstrap5 import FloatingField

import json

class Html5DateInput(forms.DateInput):
	input_type = 'date'
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.format = ('%Y-%m-%d')

class SearchForm(forms.Form):
	search = forms.CharField(required=False, label="", help_text="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Buscar...','autocomplete':'off'}))
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'get'
		self.helper.layout = Layout(
			Row(
				Column('search'),
			)
		)
		self.helper.form_tag = False
		self.helper.csfr = False

class ListSearchView(ListView):
	form_class = SearchForm
	fields_search = []
	#ordering = '-id'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class()
		if self.request.GET:
			context['form'] = self.form_class(self.request.GET)
		return context
	def get(self, *args, **kwargs):
		self.search = None
		if self.request.method == "GET" and 'search' in self.request.GET:
			form = self.form_class(self.request.GET)
			if form.is_valid():
				self.search = form.cleaned_data['search']
				#if self.search=='':
				#	return HttpResponseRedirect(self.request.path)
		redirect = self.get_page_object_is_on()
		if(redirect):
			return redirect
		return super().get(*args, **kwargs)
	def search_fields(self, query):
		search = self.search
		if (search and len(self.fields_search)!=0):
			trigram = None
			for field in self.fields_search:
				#self.model._meta.get_field(field)
				if trigram==None:
					trigram = TrigramSimilarity(Coalesce(Cast(field, CharField()), Value('')),search)
				else:
					trigram = trigram + TrigramSimilarity(Coalesce(Cast(field, CharField()),Value('')),search)
			return query.annotate(
				similarity = trigram
			).order_by('-similarity')
		else:
			return query
	def get_queryset(self):
		query = super().get_queryset()
		return self.search_fields(query)
	def get_page_object_is_on(self):
		if self.request.method == 'GET':
			if('idpage' in self.request.GET and hasattr(self, 'paginate_by')):
				idpage = int(self.request.GET['idpage'])
				idoriginalobj = int(self.request.GET['idoriginalobj'] if self.request.GET.get('idoriginalobj','')!='' else idpage)
				redirectlistnameid = self.request.GET.get('redirectlistnameid','')
				query = self.get_queryset().values_list('id', flat=True)
				model_ids = list(query)
				page = model_ids.index(idpage) // self.get_paginate_by(self.get_queryset()) + 1
				return HttpResponseRedirect(self.request.path + '?page=' + str(page) + '#' + redirectlistnameid + str(idoriginalobj))
			else:
				return None
		else:
			return None

class FormPageRedirectView(FormView):
	#needs self.object
	#redirect_list_name_id -> encargado de saber si el identificador tiene un nombre añadido no se usa con delete
	#redirect_location -> se usa el id del modelo de las lista para determinar la pagina por defecto no se nesesita 
	#amenos que se haga un tree list en cuyo caso el objeto no conteien el id del modelo para la redireccion
	#redirect_if_delete -> solo en caso de borrado
	def get_success_url(self):
		#import pdb; pdb.set_trace()
		if(hasattr(self, 'redirect_location')):
			retriever = attrgetter(self.redirect_location)
			add = '?idpage=' + str(retriever(self.object))
			if(not(getattr(self,'redirect_if_delete',False))):
				add = add + '&idoriginalobj=' + str(self.object.id)
		else:
			add =  '?idpage=' + str(self.object.id)
			#add = add + '&idoriginalobj=' + str(self.object.id)
		if(hasattr(self, 'redirect_list_name_id')):
			add = add + '&redirectlistnameid=' + getattr(self,'redirect_list_name_id','')
		return super().get_success_url() + add

class ModelExtraView(FormView):
	#model_extra
	def get_context_data(self, *args , **kwargs):
		context = super().get_context_data(*args, **kwargs)
		if 'object_extra' not in context and hasattr(self, 'model_extra'):
			context['object_extra'] = self.model_extra.objects.get(id=self.kwargs['pk'])
		return context

class CreateViewInternal(CreateView, ModelExtraView):
	#location -> solo para redireccionar
	def get_success_url(self):
		retriever = attrgetter(self.location)
		return reverse_lazy(self.success_url,kwargs={'pk':retriever(self.object)})
	def form_valid(self, form):
		setattr(form.instance, self.model_extra.__name__.lower(), self.get_context_data()['object_extra'])
		return super().form_valid(form)

class UpdateViewInternal(UpdateView):
	#location -> solo para redireccionar
	def get_success_url(self):
		retriever = attrgetter(self.location)
		return reverse_lazy(self.success_url,kwargs={'pk':retriever(self.object)})

class DeleteViewInternal(DeleteView):
	#location -> solo para redireccionar
	def get_success_url(self):
		retriever = attrgetter(self.location)
		return reverse_lazy(self.success_url,kwargs={'pk':retriever(self.object)})

def extra_field_inlineformset(request,formset):
	if(issubclass(requerimientof_inlinev2,BaseInlineFormSet)):
		raise Http404("no es un inline")
	return render(request, 'base/extra_field.html',{})

def auto_size_openpyxl(ws):
	for col in ws.columns:
		max_length = 0
		column = col[0].column_letter # Get the column name
		for cell in col:
			try: # Necessary to avoid error on empty cells
				if len(str(cell.value)) > max_length:
					max_length = len(str(cell.value))
			except:
				pass
		adjusted_width = (max_length + 2) * 1.2
		ws.column_dimensions[column].width = adjusted_width

def add_titles_openpyxl(ws, titulos):
	for idx, t in enumerate(titulos):
		ws.cell(row=1, column=(idx+1)).value = t 

#por ahora solo funciona si no se a reescrito la lista en el query
def get_page_object_is_on(list_view, id):
	if(not list_view.paginate_by):
		return 1
	query = list_view.get_queryset().values_list('id', flat=True)
	model_ids = list(query)
	return model_ids.index(id) // list_view.paginate_by + 1

#limpiar json
def clean_json_by_key(array_fields_delete, array):
	for a in array.copy():
		for d in array_fields_delete:
			try:
				del a[d]
			except Exception as e:
				print(e)
	return array
