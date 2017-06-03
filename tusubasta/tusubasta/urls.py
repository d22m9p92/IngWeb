from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from login.views import *
from sitio.views import *
#from . import views
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'tusubasta.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<idCategoria>\d*)$', home.as_view(), name='home'),
    url(r'^robots\.txt/$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    url(r'', include('login.urls')),
    url(r'', include('sitio.urls')),
]
