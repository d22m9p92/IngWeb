from django.conf.urls import include, url
from django.contrib import admin
from login.views import *


urlpatterns = [
    # Examples:
    # url(r'^$', 'tusubasta.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home.as_view()),
    #url(r'^login/$', login.as_view()),
    #url(r'^login/$', 'login.views.login_aplication')
    url(r'', include('login.urls'))
    #url(r'^registrar/$', registrar.as_view()),
]
