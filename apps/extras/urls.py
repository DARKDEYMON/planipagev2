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

app_name = 'extras' 

urlpatterns = [
    path('listpaginas/', permission_required('users.extras')(login_required(ListPaginaView.as_view())), name='list_paginas'),
    path('createpaginas/', permission_required('users.extras')(login_required(CreatePaginaView.as_view())), name='create_paginas'),
    path('updatepaginas/<int:pk>/', permission_required('users.extras')(login_required(UpdatePaginaView.as_view())), name='update_paginas'),
    path('deletepagina/<int:pk>/', permission_required('users.users')(login_required(DeletePaginaView.as_view())), name='delete_pagina'),
   #miebros
    path('miembro/', permission_required('users.extras')(login_required(ListMiembroView.as_view())), name='miembro_list'),
    path('miembro/create/', permission_required('users.extras')(login_required(CreateMiembroView.as_view())), name='miembro_create'),
    path('miembro/update/<int:pk>/', permission_required('users.extras')(login_required(UpdateMiembroView.as_view())), name='miembro_update'),
    path('miembro/delete/<int:pk>/', permission_required('users.extras')(login_required(DeleteMiembroView.as_view())), name='miembro_delete'),
]