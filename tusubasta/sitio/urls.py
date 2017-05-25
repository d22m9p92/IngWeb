from django.conf.urls import include, url
from django.contrib import admin
from . import views
from .views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'tusubasta.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^aboutUs/$', views.aboutUs),
    url(r'^nuevasubasta/$', views.nuevaSubasta, name='nuevaSubasta'),
	url(r'^subasta/(?P<pk>[0-9]+)/$', views.subasta_detalle, name='subastadetalle'),
	url(r'^ofertar/(?P<pk>[0-9]+)/$', views.ofertar, name='ofertar'),
	url(r'^ofertavalida/$', views.ofertavalida, name='ofertavalida'),
	url(r'^listaSubastas/$', views.listarSubastas, name='listarSubastas'),
	url(r'^editarSubasta/(?P<idSubasta>\w+)/$', views.editarSubasta, name='editarSubasta'),
	url(r'^eliminarSubasta/$', views.eliminarSubasta, name='eliminarSubasta'),
	url(r'^comentar/$', views.comentar, name='comentar'),
	url(r'^eliminarComentario/$', views.eliminarComentario, name ='eliminarComentario'),
	url(r'^denunciarComentario/(?P<pk>[0-9]+)/$$', views.denunciarComentario, name ='denunciarComentario'),

]
