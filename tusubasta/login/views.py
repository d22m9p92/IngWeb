# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout as auth_logout #ver esto
from django.contrib import auth
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from .form import *
#from django.core.context_processors import csrf
from sitio.models import Subastas
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import FormView, TemplateView, RedirectView
from django.core.mail import send_mail
from django.utils import timezone
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.shortcuts import get_object_or_404
from login.models import Perfil
import hashlib, datetime, random
import os, string
global str

class LoginView(FormView):
    # Le indicamos que el formulario a utilizar es el formulario de autenticación de Django
    form_class = AuthenticationForm
    # Establecemos la plantilla a utilizar
    template_name = "login.html"
    #Le decimos que cuando se haya completado exitosamente la operación nos redireccione a la url productos
    success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            # Si el usuario está autenticado entonces nos direcciona a la url establecida en success_url
            return HttpResponseRedirect(self.get_success_url())
        else:
            # Si no lo está entonces nos muestra la plantilla del login simplemente
            return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect("/")


def registrar(request):
    if request.method=='POST':
        #if not User.objects.filter(username=request.POST['username']):
         #Se verifica que no sea repetido
        if request.POST['password'] == request.POST['confpassword']:
            nickname        = request.POST['nickName']
            nombre          = request.POST['nombre']
            apellido        = request.POST['apellido']
            email           = request.POST['email']
            password        = request.POST['password']
            user            = User.objects.create_user(username=nickname, email=email, password=password, first_name=nombre, last_name=apellido)
            user.is_active  = False
            
            #Generacion de Token en el Perfil
            N               = 20
            token           = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))
            perfil          = Perfil(usuario = user, activacion_token = token)

            ##Enviar mail de confirmación
            email_subject   = 'Confirmación de cuenta TuSubasta'
            email_body      = "Hola %s, Gracias por registrarte. Para activar tu cuenta da clíck en este link en menos de 48 horas: http://127.0.0.1:8000/confirmar/%s" % (nombre, token)
            
            send_mail(email_subject,email_body, 'tusubastas2017@gmail.com',[email] )

            user.save()
            perfil.save()

            #send_registration_confirmation(user)
            return HttpResponseRedirect("/validacionmail/")
        else:
            return('contraseña incorreca')
        #else:
        #    return('mail ya existente')
    else:
        form = formRegistrar()
    return render(request,'registrar.html', { 'form': form })


def confirmar(request, activacion_token):
    perfil_usuario  = get_object_or_404(Perfil, activacion_token = activacion_token )    
    user            = perfil_usuario.usuario
    user.is_active  = True
    user.save()
    return HttpResponseRedirect("/")


def validacionmail(request):
    return render(request, 'validacionmail.html')





