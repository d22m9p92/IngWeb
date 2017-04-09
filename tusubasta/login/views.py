from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, login, logout as auth_logout #ver esto
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .form import formRegistrar
from .form import formLogin


# Create your views here.

class home(View):
    def get(self, request):
        return render(request, "index.html")


def login_aplicacion(request):
    message = None
    context = RequestContext(request, { 'request': request, 'user': request.user})
    return render_to_response('login.html', context_instance=context)

    if request.method=='POST':
        user = request.POST['email']
        password = request.POST['password']
        usuario = authenticate(email=email, password=password)
        if usuario is not None:
            if usuario.is_active:
                auth.login(request,usuario)
                request.session['usrLogueado']=user
                msg = "Te has identificado correctamente"
               #return redirect("/miembros/")
                #redireccionar a admin
            else:
                msg = "Usuario inactivo"
                #return redirect(reverse('Registro.views.login'))
        else:
            msg = 'Nombre de usuario y/o contraseña es incorrecto'
            #form = formLogin()
            #form2 = formRegistro()
            #return render(request,'login.html', {"form":form, "formR":form2})
    else:
        form = formLogin()
        #form2 = formRegistro()
    return render(request,'login.html', {"message":msg, 'form': form })
    #return render(request,'login.html', {"form":form, "formR":form2})