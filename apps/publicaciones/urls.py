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
    path('', main, name='main'),
    
    path('listpublicacion/', permission_required('users.publicaciones')(login_required(ListPublicacionViews.as_view())), name='publicacion_list'),
    path('createPublicacion/', permission_required('users.publicaciones')(login_required(CreatePublicacionView.as_view())), name='publicacion_create'),
    path('updatePublicacion/<int:pk>/', permission_required('users.publicaciones')(login_required(UpdatePublicacionView.as_view())), name='publicacion_update'),
    path('deletePublicacion/<int:pk>/', permission_required('users.publicaciones')(login_required(DeletePublicacionView.as_view())), name='publicacion_delete'),

    path('archivoforminline/<int:pk>/', permission_required('users.publicaciones')(login_required(archivo_form_inline_view)), name='publicaciones_inline'),

    path('listvistapublicaiones/<int:pk>/', ListVistaPublicaionesView.as_view(), name='list_vistapublicaciones'),
    path('listsearch/', ListSearchPublicaionView.as_view(), name='list_search'),
    path('detailpublicacion/<int:pk>/', DetailPublicacionView.as_view(), name='detail_publicacion'),
    path('nosotros/', nosotros_view, name='nosotros')
]