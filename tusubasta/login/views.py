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
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
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
from django.contrib import messages
global str
import json


class LoginView(FormView):
    # Le indicamos que el formulario a utilizar es el formulario de autenticación de Django
    form_class = AuthenticationForm
    # Establecemos la plantilla a utilizar
    template_name = "login.html"
    #Le decimos que cuando se haya completado exitosamente la operación nos redireccione a la url productos
    success_url = reverse_lazy('home', kwargs={'idCategoria': ""})

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            # Si el usuario está autenticado entonces nos direcciona a la url establecida en success_url
            return HttpResponseRedirect(self.get_success_url())
        else:
            # Si no lo está entonces nos muestra la plantilla del login simplemente
            return super(LoginView, self).dispatch(request, *args, **kwargs)
            #messages.error(request, "Usuario o contaseña incorrecta.")

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)


def logout(request):
    try:
        print("ok")
        auth_logout(request)
    except Exception as e:
        print(e)
    return HttpResponseRedirect("/")


def registrar(request):
    if request.method=='POST':
        form = formRegistrar(request.POST)
        if not User.objects.filter(username=request.POST['nickName']).exists():
            if not User.objects.filter(email=request.POST['email']).exists():
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
                    email_body      = "Hola %s, Gracias por registrarte. Para activar tu cuenta haga clíck en este link: /n https://tusubasta.herokuapp.com/bienvenido/%s" % (nombre, token)
                    
                    send_mail(email_subject,email_body, 'tusubastas2017@gmail.com',[email] )

                    user.save()
                    perfil.save()

                    #send_registration_confirmation(user)
                    return HttpResponseRedirect("/validacionmail/")
                else:
                    messages.error(request, "Las contraseñas no coinciden.")
            else:
                messages.error(request, "El mail ya pose una cuenta asociada.")
        else:
            messages.error(request, "Usuario ya registrado.")
    else:
        form = formRegistrar()
    return render(request,'registrar.html', { 'form': form })


def confirmar(request, activacion_token):
    perfil_usuario  = get_object_or_404(Perfil, activacion_token = activacion_token )    
    user            = perfil_usuario.usuario
    user.is_active  = True
    user.save()
    return render(request, 'bienvenido.html')


def validacionmail(request):
    return render(request, 'validacionmail.html')


def cambiarContraseña(request):
    if not request.POST['email']:
        messages.warning(request, "Por favo ingresar mail.")
    return render(request,'registrar.html', { 'form': form })        


@login_required(login_url="home")
def verPerfil(request,pk):
    usuario = User.objects.get(pk=pk)
    perfil  = Perfil.objects.get(usuario=usuario)
    return render(request,"perfil.html",{'usuario': usuario, 'perfil': perfil})


@login_required(login_url="home")
def editarUsuario(request,pk):
    if request.method =="POST":
        usuario = User.objects.get(pk=pk)
        form = formUsuario(request.POST, instance = usuario)
        if form.is_valid():
            form.save()
            perfil = Perfil.objects.get(usuario= usuario)
            formP = formPerfil(instance= perfil)
            formU = formUsuario(instance=usuario)
            #message.success(request, "Los datos han sido modificados correctmaente")
            return render(request, "editPerfil.html", {'usuario': formU, 'perfil': formP,"id":perfil.id,"idUsuario":usuario.id})
        else:
            perfil = Perfil.objects.get(usuario= usuario)
            formP = formPerfil(instance= perfil)
            formU = formUsuario(instance=usuario)
            return render(request, "editPerfil.html", {'usuario': formU, 'perfil': formP,"id":perfil.id,"idUsuario":usuario.id})
   


@login_required(login_url="home")
def editarPerfil(request,pk):
    if request.method=="GET":
            perfil = Perfil.objects.get(pk=pk)
            usuario = perfil.usuario

            formP = formPerfil(instance= perfil)
            formU = formUsuario(instance=usuario)
            return render(request, "editPerfil.html", {'usuario': formU, 'perfil': formP,"id":pk,"idUsuario":usuario.id})

    elif request.method == "POST":
        perfil = Perfil.objects.get(pk=pk)
        formPG = formPerfil(request.POST,instance=perfil)

        try:
            if formPG.is_valid():
                formPG.save()
                perfil = Perfil.objects.get(pk=pk)
                usuario = perfil.usuario
                formP = formPerfil(instance= perfil)
                formU = formUsuario(instance=usuario)   
                return render(request, "editPerfil.html", {'usuario': formU, 'perfil': formP,"id":pk,"idUsuario":usuario.id}) 
            else:
                perfil = Perfil.objects.get(pk=pk)
                usuario = perfil.usuario
                formP = formPerfil(instance = perfil)
                formU = formUsuario(instance=usuario)    
                return render(request, "editPerfil.html", {'usuario': formU, 'perfil': formP,"id":pk, "idUsuario":usuario.id})
        except Exception as e:
            perfil = Perfil.objects.get(pk=pk)
            usuario = perfil.usuario
            formP = formPerfil(instance= perfil)
            formU = formUsuario(instance=usuario)    
            return render(request, "editPerfil.html", {'usuario': formU, 'perfil': formP,"id":pk,"idUsuario":usuario.id})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Su contraseña se modificó correctamente')
            return redirect('home', "")
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})


def olvidoPass(request):
    if request.method == 'POST':
        form    = OlvidoContraseña(request.POST)
        email   = request.POST.get("email")
        
        try:
            
            usuario = User.objects.get(email = email)
            nombre  = usuario.first_name
            activo  = usuario.is_active 
            pk      = usuario.id 
            
            if activo == True:
                
                if form.is_valid():
                    print('bien')
                    N                       = 20
                    token                   =   ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))
                    perfil                  = Perfil.objects.get(usuario_id = pk)
                    perfil.olvido_token     = token
                    perfil.save()
                    email_subject           = 'Cambio de contraseña'
                    email_body              = "Hola %s, para cambiar tu contraseña ingresa al siguiente link https://tusubasta.herokuapp.com/recuperarpass/%s" % (nombre, token)

                    send_mail(email_subject,email_body, 'tusubastas2017@gmail.com',[email] )


                    email_subject   = 'Confirmación de cuenta TuSubasta'
                    email_body      = "Hola %s, Gracias por registrarte. Para activar tu cuenta haga clíck en este link: /n https://tusubasta.herokuapp.com/bienvenido/%s" % (nombre, token)
                    
                    send_mail(email_subject,email_body, 'tusubastas2017@gmail.com',[email] )



                    return HttpResponseRedirect("/olvidomsg/")
            else:
                messages.error(request, "El usuario no se encuentra activo.")

        except User.DoesNotExist:
            usuario = None
            if usuario == None:
                messages.error(request, "La cuenta de mail no se encuentra registrada.")
    else:
        form = OlvidoContraseña()
    return render(request, 'olvidopass.html', {'form': form})


def olvidomsg(request):
    return render(request, 'olvidomsg.html')


def renovarpass(request, token):
    if request.method == 'POST':
        form    	= renovarContraseña(request.POST)
        contra  	= request.POST.get('password')
        confpass 	= request.POST.get('confpassword')
        #try:
        if form.is_valid():
        	if contra == confpass:
        		
	            perfil  = Perfil.objects.get(olvido_token = token)
	            print(perfil.usuario_id)
	            usuario = User.objects.get(pk = perfil.usuario_id)
	            print(usuario.id)
	            usuario.set_password(contra)
	            usuario.save()
	            perfil.olvido_token	= None
	            perfil.save()
	            return render(request, 'recuperomsg.html') 
	        else:
	        	messages.error(request, "La contraseñas no coinciden.")

    else:
        form = renovarContraseña()
    return render(request, 'renovarpass.html' ,{'form': form, "token": token}) 


@login_required(login_url= '/login/')
def listarUsuariosBloqueados(request):
    if request.method == 'GET':
        _idUsuario  = request.user.id
        usuarios = User.objects.select_related("perfil").filter(is_active=False, perfil__fechaBaja=None).distinct()
        listaUsuariosBloqueados = []

        for u in usuarios:
            listaUsuariosBloqueados.append(u)
            
        return render(request, 'listausuariosbloqueados.html', {'listaUsuariosBloqueados': listaUsuariosBloqueados})


@login_required(login_url= '/login/')
def eliminarUsuario(request):
    if request.method =="POST":
        id = request.POST.get("id")
        try:
            perfil = Perfil.objects.get(id=id)
            fb = datetime.datetime.now()
            perfil.fechaBaja = fb
            perfil.save()
            return HttpResponse(json.dumps("OK"))
        except Exception  as e:
            return HttpResponse(json.dumps(str(e)))

def restaurarUsuario(request):
    if request.method =="POST":
        id = request.POST.get("id")
        try:
            usuario = User.objects.get(pk=id)
            usuario.is_active = True
            usuario.save()
            return HttpResponse(json.dumps("OK"))
        except Exception as e:
            return HttpResponse(json.dumps(str(e))) 