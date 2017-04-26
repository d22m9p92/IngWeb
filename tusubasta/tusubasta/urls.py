from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from login.views import *
from . import views
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'tusubasta.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home.as_view(), name='home'),
    url(r'', include('login.urls')),
    url(r'^productos/$', views.productos, name='productos'),

]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	