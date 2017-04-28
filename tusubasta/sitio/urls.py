from django.conf.urls import include, url
from django.contrib import admin
from . import views
from .views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'tusubasta.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^nuevasubasta/$', views.nuevaSubasta, name='nuevaSubasta'),
	url(r'^listasubasta/$', views.SubastaList.as_view(), name='listasubasta'),
]
