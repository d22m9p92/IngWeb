from django.conf.urls import include, url
from django.contrib import admin
from . import views
from .views import *

urlpatterns = [
    
    url(r'^aboutUs/$', views.aboutUs),
	url(r'^ofertar/(?P<pk>[0-9]+)/$', views.ofertar, name='ofertar'),
	url(r'^ofertavalida/$', views.ofertavalida, name='ofertavalida'),
	url(r'^moderador/$', views.moderador, name ='moderador'),

	#Publicaciones
	url(r'^subasta/(?P<pk>[0-9]+)/$', views.subasta_detalle, name='subastadetalle'),
	url(r'^nuevasubasta/$', views.nuevaSubasta, name='nuevaSubasta'),
	url(r'^listaSubastas/$', views.listarSubastas, name='listarSubastas'),
	url(r'^editarSubasta/(?P<idSubasta>\w+)/$', views.editarSubasta, name='editarSubasta'),
	url(r'^denunciarSubasta/(?P<pk>[0-9]+)/$$', views.denunciarSubasta, name ='denunciarSubasta'),
	url(r'^listasubastasdenunciadas/$', views.listarSubastasDenunciadas),
	url(r'^listasubastaseliminadas/$', views.listarSubastasEliminadas),
	url(r'^restaurarSubasta/$', views.restaurarSubasta, name ='restaurarSubasta'),
	url(r'^eliminarSubasta/$', views.eliminarSubasta, name='eliminarSubasta'),

	#Comentarios
	url(r'^comentar/$', views.comentar, name='comentar'),
	url(r'^denunciarComentario/(?P<pk>[0-9]+)/$$', views.denunciarComentario, name ='denunciarComentario'),
	url(r'^listacomentariosdenunciados/$', views.listarComentariosDenunciados),
	url(r'^listacomentarioseliminados/$', views.listarComentariosEliminados),
	url(r'^eliminarComentario/$', views.eliminarComentario, name ='eliminarComentario'),
	url(r'^restaurarComentario/$', views.restaurarComentario, name ='restaurarComentario'),

]
