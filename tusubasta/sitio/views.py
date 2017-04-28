from django.shortcuts import render, render_to_response, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout as auth_logout #ver esto
from django.contrib import auth
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .form import *
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from .models import *
from django.views.generic import ListView


def SubastaL(request):
    subastas = Subasta.objects.all()
    return render(request,"index.html",{"productos": subastas})

class SubastaList(ListView):
	model = Subastas

def nuevaSubasta(request):
	if request.method=='POST':
		form = SubastasForm(request.POST)
		if form.is_valid():
			nueva_subasta = form.save()
			return HttpResponse("/nuevasubastas/")	
			#return HttpResponseRedirect(reverse())
	else:
		form = SubastasForm()

	return render(request,'nuevasubasta.html', { 'form': form })

'''
def registrar(request):
    if request.method=='POST':
        #form = formRegistro(request.POST)
        #if not User.objects.filter(username=request.POST['username']):
         #Se verifica que no sea repetido
        if request.POST['password'] == request.POST['confpassword']:
            usuario = request.POST['nickName']
            nombre = request.POST['nombre']
            apellido = request.POST['apellido']
            email = request.POST['email']
            password = request.POST['password']
            user = User.objects.create_user(username=usuario, email=email, password=password, first_name=nombre, last_name=apellido)
            user.is_active = False
            user.save()
            #send_registration_confirmation(user)
            #return render(request, 'index.html')
            #return HttpResponseRedirect("/admin/")
            return HttpResponse("/admin/")

        else:
            #return HttpResponseRedirect("/registrar/")
            return HttpResponse({'Contraseña': 'incorrecta'})
        #else:
        	#return render(request, 'registrar.html')#'mail ya existente'
    else:
    	form = formRegistrar()
    return render(request,'registrar.html', { 'form': form })
    

# Create your views here.
'''