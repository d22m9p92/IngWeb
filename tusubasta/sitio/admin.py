from django.contrib import admin
from .models import *
from login.models import *

# Register your models here.

admin.site.register(Subastas)
admin.site.register(Perfil)
admin.site.register(Comentarios)
admin.site.register(MotivosDenuncias)
admin.site.register(TiposUsuarios)
admin.site.register(Categorias)
admin.site.register(Denuncias)