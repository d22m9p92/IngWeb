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
            form = formLogin()
            #form2 = formRegistrar()
    else:
        form = formLogin()
        #form2 = formRegistro()
    return render(request,'login.html', { 'form': form })
    #return render(request,'login.html', {"form":form, "formR":form2})


def registrar(request):
    if request.method=='POST':

        #if not User.objects.filter(username=request.POST['username']):
         #Se verifica que no sea repetido
        if request.POST['password'] == request.POST['confpassword']:
            nickname = request.POST['nickName']
            nombre = request.POST['nombre']
            apellido = request.POST['apellido']
            email = request.POST['email']
            password = request.POST['password']
            user = User.objects.create_user(username=nickname, email=email, password=password, first_name=nombre, last_name=apellido)
            user.is_active = False
            user.save()
            #send_registration_confirmation(user)
            #return render(request, 'index.html')
            return HttpResponseRedirect("/productos/")
        else:
            return('contraseña incorreca')
        #else:
        #    return('mail ya existente')
    else:
        form = formRegistrar()
    return render(request,'registrar.html', { 'form': form })