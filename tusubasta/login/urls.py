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
    url(r'^perfil/(?P<id>\w+)/', views.verPerfil, name='perfil')
    # url(r'^perfil/$', views.perfil),
    # url(r'^perfil/(?P<pk>[0-9]+)/$', views.perfil),

]
