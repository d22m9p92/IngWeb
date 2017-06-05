from django.conf.urls import include, url
from django.contrib import admin
from . import views
from .views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'tusubasta.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^logout/$', views.logout),
    url(r'^registrar/$', views.registrar),
    url(r'^login/$', LoginView.as_view()),
    url(r'^confirmar/(?P<activacion_token>\w+)/', views.confirmar),
    url(r'^validacionmail/$', views.validacionmail),
    url(r'^perfil/(?P<pk>\d+)/', views.verPerfil, name='perfil'),
    url(r'^editarperfil/(?P<pk>\d+)/$', views.editarPerfil, name= 'editarperfil'),
    url(r'^editarUsuario/(?P<pk>\d+)/$', views.editarUsuario, name='editarusuario'),
    url(r'^password/$', views.change_password, name='change_password'),
    url(r'^olvidopass/$', views.olvidoPass),
    url(r'^olvidomsg/$', views.olvidomsg, name='olvidomsg'),
    url(r'^renovarpass/(?P<token>\w+)/', views.renovarpass, name='renovarpass'),
    url(r'^listausuariosbloqueados/$', views.listarUsuariosBloqueados),
    url(r'^eliminarusuario/$', views.eliminarUsuario),
    url(r'^restaurarusuario/$', views.restaurarUsuario),
    url(r'^bienvenido/', views.bienvenido),
    
]
