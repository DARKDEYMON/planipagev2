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
    path('controlmaestroslist/', login_required(ControlMaestrosListView.as_view()), name='controlmaestros_list'),
    path('controltipolist/<int:pk>/', login_required(ControlTipoListView.as_view()), name='controltipo_list'),
    path('controlpublicacionlist/<int:pk>/', login_required(ControlPublicacionListView.as_view()), name='controlpublicacion_list'),
    path('controlupdatepublicacion/<int:pk>/', login_required(ControlUpdatePublicacionView.as_view()), name='control_updateublicacion'),
    path('controlarchivosinline/<int:pk>/', login_required(control_archivo_form_inline_view), name='control_archivos_inline'),
    path('controlcreatepublicacion/', login_required(ControlCreatePublicacionView.as_view()), name='control_create_publicacion')
]
