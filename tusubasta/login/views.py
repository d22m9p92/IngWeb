from django.shortcuts import render, render_to_response, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout as auth_logout #ver esto
from django.contrib import auth
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .form import *
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.

class home(View):
    def get(self, request):
        return render(request, "index.html")

def login_aplicacion(request):
    if request.method=='POST':
        user = request.POST['username']
        password = request.POST['password']
        usuario = authenticate(username=user, password=password)
        if usuario is not None:
            if usuario.is_active:
                auth.login(request,usuario)
                #msg = "Te has identificado correctamente"
                return HttpResponseRedirect("/admin/")
            else:
                msg = "Usuario inactivo"
                #return redirect(reverse('Registro.views.login'))
        else:
            msg = 'Nombre de usuario y/o contraseña es incorrecto'
            #return msg
            form = formLogin()
            #form2 = formRegistrar()
            #return render(request,'login.html', {'mensaje' : mensaje})
    else:
        form = formLogin()
        #form2 = formRegistro()
    return render(request,'login.html', { 'form': form })
    #return render(request,'login.html', {"form":form, "formR":form2})
