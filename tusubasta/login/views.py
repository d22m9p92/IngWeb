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


"""
def login(request):
    context = RequestContext(request, { 'request': request, 'user': request.user})
    return render_to_response('login.html', context_instance=context)
if request.method=='POST':
    user = request.POST['email']
    passw = request.POST['password']
    usuario = authenticate(username=user, password=passw)
    if usuario is not None:
        if usuario.is_active:
            auth.login(request,usuario)
            request.session['usrLogueado']=user
            return redirect("/miembros/")
        else:
            return redirect(reverse('Registro.views.login'))
    else:
        form = formLogin()
        form2 = formRegistro()
        return render(request,'login.html', {"form":form, "formR":form2})
else:
    form = formLogin()
    form2 = formRegistro()
    return render(request,'login.html', {"form":form, "formR":form2})
"""