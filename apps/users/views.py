from django.shortcuts import render
from .generic import *
from .forms import *

# Create your views here.

class ListUserView(ListSearchView):
	model = User
	ordering = ['id']
	paginate_by = 10
	template_name = 'users/list_users.html'
	fields_search = ['id','username','first_name','last_name','email','ci']
	def get_queryset(self):
		query = super().get_queryset().filter(is_staff=False)
		return query

class CreateUserView(CreateView, FormPageRedirectView):
	form_class = CreateUserForm
	template_name = 'users/create_user.html'
	success_url = reverse_lazy('users:list_user')


class PermisosView(FormPageRedirectView):
	model = User
	model_permissions = User
	form_class = AddPermissionsForm
	template_name = 'users/permisos.html'
	success_url = reverse_lazy('users:list_user')
	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		kwargs['model_permissions'] = self.model_permissions
		return kwargs
	def get_initial(self):
		pk = self.kwargs.get('pk',0)
		self.user = self.model.objects.get(id=pk)
		self.object = self.user
		content_type = ContentType.objects.get_for_model(self.model_permissions)
		permisos_actuales = self.user.user_permissions.filter(content_type=content_type)
		perms = {}
		for p in permisos_actuales:
			perms[p.codename] = True
		return perms
		#return { 'usuarios': True, 'academico': False }
	def form_valid(self, form):
		if form.is_valid():
			data = form.cleaned_data
			for p in data:
				content_type=ContentType.objects.get_for_model(self.model_permissions)
				permission = Permission.objects.get(content_type=content_type, codename=p)
				if data[p]:
					self.user.user_permissions.add(permission)
				else:
					self.user.user_permissions.remove(permission)
		return super().form_valid(form)

class ConstanceView(FormView):
	form_class = ConstanceForm
	template_name = 'constance.html'
	success_url = '/'
	def form_valid(self, form):
		if form.is_valid():
			form.save()
		return super().form_valid(form)