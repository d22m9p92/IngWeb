from django.shortcuts import render, render_to_response, redirect, get_object_or_404
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
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Max
from django.contrib import messages

class home(View):
    def get(self, request): 
        subastas = Subastas.objects.all()
        categorias = Categorias.objects.all()
        
        paginator = Paginator(subastas, 12)

        page = request.GET.get('page')
        try:
            SubastasList = paginator.page(page)
        except PageNotAnInteger:
            SubastasList = paginator.page(1)
        except EmptyPage:
            SubastasList = paginator.page(paginator.num_pages)        
        
        return render(request, "index.html",{"subastas": SubastasList, "categorias": categorias})

#Crear una Subasta
@login_required(login_url= '/login/')
def nuevaSubasta(request):
    if request.method=='POST':
        form = SubastasForm(request.POST)
        _idUsuarioVendedor = request.user.id
        if form.is_valid():
            formSubasta = form.save(commit = False)
            formSubasta.idUsuarioVendedor_id = _idUsuarioVendedor
            formSubasta.save()
            return HttpResponseRedirect("/")	
            #return HttpResponseRedirect(reverse())
    else:
        form = SubastasForm()
    return render(request,'nuevasubasta.html', { 'form': form })

#View de una subasta
@login_required(login_url= '/login/')
def subasta_detalle(request, pk):
    subasta = get_object_or_404(Subastas, pk=pk)
    return render(request, 'subasta_detalle.html', {'subasta': subasta})


@login_required(login_url= '/login/')
def editarSubasta(request, idSubasta):
    if request.method == 'GET':
        form = SubastasForm(request.POST, instance = Subasta)
        if form.is_valid():
            Subasta  = Subastas.objects.get(pk = idSubasta)
        
    else:
        Subasta  = Subastas.objects.get(pk = idSubasta)
        formSubastaEdit = SubastasForm(instance = Subasta)


#Ofertar en una subasta
@login_required(login_url= '/login/')
def ofertar(request,pk):
    
    if request.method == 'POST':
        form        = OfertarForm(request.POST)
        _idSubasta  = int(request.POST.get("idSubasta"))
        _idUsuario  = request.user.id
        if form.is_valid():
            if int(request.POST.get("valorOferta")) >= (maximaOferta(int(request.POST.get("idSubasta"))) + 10 ):
                formOferta                      = form.save(commit=False)
                formOferta.idSubasta_id         = _idSubasta
                formOferta.ganador              = False
                formOferta.usuarioComprador_id  = _idUsuario 
                formOferta.save()
                #ofertavalida(request)
                return render(request, 'ofertavalida.html')
            else:
                messages.error(request, "La oferta debe superar minimamente en $10 al precio actual ")
    else:
        form        = OfertarForm()
    precioActual    = maximaOferta(int(pk))
    return render(request,'ofertar.html', { 'form': form, "idSubasta": pk, "precioActual": precioActual  })


#Buscar oferta maxima
def maximaOferta(idSubasta):
    maximaOferta    = Ofertas.objects.filter(idSubasta = idSubasta).aggregate(Max('valorOferta'))
    resultado       = maximaOferta['valorOferta__max']
    if resultado is None:
        precioBase = Subastas.objects.get(pk= idSubasta).precioBase
        return precioBase
    return resultado


#Mensaje Oferta Valida 
def ofertavalida(request):
    return render(request, 'ofertavalida.html')


def listarSubastas(request):
    if request.method == 'GET':
        _idUsuario      = request.user.id 
        listaSubastas   = Subastas.objects.filter(idUsuarioVendedor_id = _idUsuario).order_by('-fechaAlta')
        return render(request, 'listaSubastas.html', {'listaSubastas': listaSubastas})
        
    



