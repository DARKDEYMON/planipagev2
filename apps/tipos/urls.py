"""
URL configuration for planipage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required
from .views import *

urlpatterns = [ 
    path('listmaestro/', permission_required('users.tipos')(login_required(ListTipoMaestroView.as_view())), name='maestro_list'),
    path('createmaestro/', permission_required('users.tipos')(login_required(CreateTipoMaestroView.as_view())), name='maestro_create'),
    path('updatemaestro/<int:pk>/', permission_required('users.tipos')(login_required(UpdateTipoMaestroView.as_view())), name='maestro_update'),
    path('deletemaestro/<int:pk>/', permission_required('users.tipos')(login_required(DeleteTipoMaestroView.as_view())), name='maestro_delete'),
    
    path('tipolist/<int:pk>/', permission_required('users.tipos')(login_required(ListTipoView.as_view())), name='tipo_list'),
    path('createtipo/<int:pk>', permission_required('users.tipos')(login_required(TipoCreateView.as_view())), name='tipo_create'),
    path('updatetipo/<int:pk>/', permission_required('users.tipos')(login_required(TipoUpdateView.as_view())), name='tipo_update'),
    path('deletetipo/<int:pk>/', permission_required('users.tipos')(login_required(TipoDeleteView.as_view())), name='tipo_delete'),
]