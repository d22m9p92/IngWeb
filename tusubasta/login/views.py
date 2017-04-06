from django.shortcuts import render
from django.views import View 
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .form import formRegistro

# Create your views here.

class home(View):
	def get(self, request):
		fRegistro = formRegistro()
		return render(request, "index.html", {"form": fRegistro })

	def post(self, request):
		email = request.POST.get("email")
		print(email)

#class login_aplicacion(View):
#	def 
