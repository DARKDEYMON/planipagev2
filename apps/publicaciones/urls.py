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
    
    path('listPublicacion/', permission_required('users.extras')(login_required(ListPublicacionViews.as_view())), name='publicacion_list'),
    path('createPublicacion/', permission_required('users.extras')(login_required(CreatePublicacionView.as_view())), name='publicacion_create'),
    path('updatePublicacion/<int:pk>/', permission_required('users.extras')(login_required(UpdatePublicacionView.as_view())), name='publicacion_update'),
    path('deletePublicacion/<int:pk>/', permission_required('users.users')(login_required(DeletePublicacionView.as_view())), name='publicacion_delete'),
]