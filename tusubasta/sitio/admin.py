from django.contrib import admin
from .models import *
from login.models import *

# Register your models here.

admin.site.register(Subastas)
admin.site.register(Perfil)