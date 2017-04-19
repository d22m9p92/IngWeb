from django.shortcuts import render, render_to_response, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout as auth_logout #ver esto
from django.contrib import auth
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from .form import *
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import FormView, TemplateView, RedirectView


# Create your views here.

class home(View):
    def get(self, request):
        return render(request, "index.html")
        

class LoginView(FormView):
    # Le indicamos que el formulario a utilizar es el formulario de autenticación de Django
    form_class = AuthenticationForm
    # Establecemos la plantilla a utilizar
    template_name = "login.html"
    #Le decimos que cuando se haya completado exitosamente la operación nos redireccione a la url productos
    success_url = reverse_lazy('productos')

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
            nickname = request.POST['nickName']
            nombre = request.POST['nombre']
            apellido = request.POST['apellido']
            email = request.POST['email']
            password = request.POST['password']
            user = User.objects.create_user(username=nickname, email=email, password=password, first_name=nombre, last_name=apellido)
            user.is_active = True
            user.save()
            #send_registration_confirmation(user)
            return render(request, 'index.html')
        else:
            return('contraseña incorreca')
        #else:
        #    return('mail ya existente')
    else:
        form = formRegistrar()
    return render(request,'registrar.html', { 'form': form })