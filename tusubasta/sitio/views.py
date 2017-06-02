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
import datetime
import json

class home(View):
    def get(self, request,idCategoria): 
        if idCategoria!="":
            categoria = Categorias.objects.filter(pk=idCategoria)
            subastas = Subastas.objects.filter(idCategoria=categoria,fechaBaja=None).order_by("-fechaAlta")
        else:    
            subastas = Subastas.objects.all().filter(fechaBaja=None)
        categorias = Categorias.objects.all()
            
        paginator = Paginator(subastas, 12)

        page = request.GET.get('page')
        try:
            SubastasList = paginator.page(page)
        except PageNotAnInteger:
            SubastasList = paginator.page(1)
        except EmptyPage:
            SubastasList = paginator.page(paginator.num_pages)        
    
        return render(request, "index.html",{"subastas": SubastasList, "categorias": categorias,"id":request.user.id })


def aboutUs(request):
    return render(request, 'aboutUs.html')

#Crear una Subasta
@login_required(login_url= '/login/')
def nuevaSubasta(request):
    if request.method=='POST':
        form = SubastasForm(request.POST)
        _idUsuarioVendedor = request.user.id
        form = SubastasForm(request.POST, request.FILES)
        if form.is_valid():
            fechaHoy    = datetime.date.today()
            fechaHoy    = fechaHoy.replace(day = int(request.POST.get('fechaFin_day'))) 
            fechaHoy    = fechaHoy.replace(month = int(request.POST.get('fechaFin_month')))
            fechaHoy    = fechaHoy.replace(year = int(request.POST.get('fechaFin_year')))
            
            if fechaHoy > datetime.date.today():
                formSubasta = form.save(commit = False)
                formSubasta.ofertaMax = formSubasta.precioBase  
                formSubasta.idUsuarioVendedor_id = _idUsuarioVendedor
                formSubasta.save()
                                
                pk     = int(formSubasta.id)
            
                return redirect("subasta_detalle", pk)
            else:
                messages.error(request, "La fecha de finalización debe ser mayor al día corriente.")
    else:
        form = SubastasForm()
    return render(request,'nuevasubasta.html', { 'form': form })



def subasta_detalle(request, pk):
    print("ok")
    subasta = get_object_or_404(Subastas, pk=pk)
    comentarios = Comentarios.objects.filter(idSubasta=subasta, fechaBaja=None).order_by("-fechaAlta")
    respuestas 	= Respuestas.objects.select_related("idComentario").filter(idComentario__idSubasta = subasta, fechaBaja = None)
    
    listaRespuestas = []
    for r in respuestas:
    	listaRespuestas.append(r)

    print(listaRespuestas)
    return render(request, 'subasta_detalle.html', {'subasta': subasta,"comentarios":comentarios, "listaRespuestas": listaRespuestas})


def listarSubastas(request):
    if request.method == 'GET':
        _idUsuario      = request.user.id 
        listaSubastas   = Subastas.objects.filter(idUsuarioVendedor_id = _idUsuario, fechaBaja = None).order_by('-fechaAlta')
        
        return render(request, 'listaSubastas.html', {'listaSubastas': listaSubastas})


@login_required(login_url= '/login/')
def editarSubasta(request, idSubasta):
    if request.method == "GET":
        subasta  = Subastas.objects.get(pk = idSubasta)
        form = SubastasForm(instance = subasta)
        
        return render(request, "editarSubasta.html", {'subasta': form,"id":idSubasta})

    elif request.method == "POST":
        subasta  = Subastas.objects.get(pk = idSubasta)
        form = SubastasForm(request.POST, request.FILES, instance = subasta)

        try:
            if form.is_valid():
                form.save()
                subasta  = Subastas.objects.get(pk = idSubasta)
                form = SubastasForm(instance = subasta)
                #return render(request, "editarSubasta.html", {'subasta': form,"id":idSubasta})
                return redirect('listarSubastas')
            else:
                subasta  = Subastas.objects.get(pk = idSubasta)
                form = SubastasForm(instance = subasta)
                return render(request, "editarSubasta.html", {'subasta': form,"id":idSubasta})
        except Exception as e:
            subasta  = Subastas.objects.get(pk = idSubasta)
            form = SubastasForm(instance = subasta)
            return render(request, "editarSubasta.html", {'subasta': form,"id":idSubasta})


def eliminarSubasta(request):
    if request.method =="POST":
        id = request.POST.get("id")
        try:
            subasta = Subastas.objects.get(pk=id)
            fb= datetime.datetime.now()
            subasta.fechaBaja = fb
            subasta.save()
            return HttpResponse(json.dumps("OK"))
        except Exception  as e:
            return HttpResponse(json.dumps(str(e)))


#Ofertar en una subasta
@login_required(login_url= '/login/')
def ofertar(request,pk):
    if request.method == 'POST':
        form        = OfertarForm(request.POST)
        _idSubasta  = int(request.POST.get("idSubasta"))
        _idUsuario  = request.user.id
        _valorOferta = int(request.POST.get("valorOferta"))
        if form.is_valid():
            if int(request.POST.get("valorOferta")) >= (maximaOferta(int(request.POST.get("idSubasta"))) + 10 ):
                formOferta                      = form.save(commit=False)
                formOferta.idSubasta_id         = _idSubasta
                formOferta.ganador              = False
                formOferta.usuarioComprador_id  = _idUsuario 
                formOferta.save()
                updateOfertaMax(_idSubasta, _valorOferta)
                return render(request, 'ofertavalida.html')
            else:
                messages.error(request, "La oferta debe superar minimamente en $10 al precio actual ")
    else:
        form        = OfertarForm()
    precioActual    = maximaOferta(int(pk))
    return render(request,'ofertar.html', { 'form': form, "idSubasta": pk, "precioActual": precioActual  })


def updateOfertaMax(Subasta, oferta):
    subasta = Subastas.objects.get(id= Subasta)
    subasta.ofertaMax = oferta
    subasta.save()

#Buscar oferta maxima
def maximaOferta(idSubasta):
    maximaOferta    = Ofertas.objects.filter(idSubasta = idSubasta).aggregate(Max('valorOferta'))
    resultado       = maximaOferta['valorOferta__max']
    if resultado is None:
        precioBase = Subastas.objects.get(pk=idSubasta).precioBase
        return precioBase
    return resultado


#Mensaje Oferta Valida 
def ofertavalida(request):
    return render(request, 'ofertavalida.html')

@login_required(login_url= '/login/')
def moderador(request):
    return render(request, 'moderador.html')

@login_required(login_url= '/login/')
def comentar(request):
    if request.method == 'POST':
        texto = request.POST.get("texto")
        idSubasta = request.POST.get("idSubasta")
        try:
           comentario = Comentarios()
           comentario.comentario = texto
           subasta = Subastas.objects.get(pk=idSubasta)
           comentario.idSubasta = subasta
           comentario.idUsuario = request.user
           comentario.fechaAlta = datetime.datetime.now()
           comentario.save()
           comentarios = Comentarios.objects.filter(idSubasta = subasta, fechaBaja=None).order_by("-fechaAlta")
           return render(request,"comentarioParcial.html",{"comentarios":comentarios})
        except Exception as e:
            return HttpResponse(json.dumps("Error"))   


@login_required(login_url= '/login/')
def responder(request):
    if request.method == 'POST':
        print("entro")
        texto 			= request.POST.get("texto")
        idComentario 	= request.POST.get("idComentario")
        try:
           respuesta = Respuestas()
           respuesta.respuesta = texto
           comentario = Comentarios.objects.get(pk=idComentario)
           respuesta.idComentario = comentario
           respuesta.idUsuario = request.user
           respuesta.fechaAlta = datetime.datetime.now()
           respuesta.save()
           respuestas = Respuestas.objects.filter(idComentario = comentario, fechaBaja=None).order_by("-fechaAlta")
           return render(request,"respuestaParcial.html",{"respuestas":respuestas})
        except Exception as e:
            print(e)
            return HttpResponse(json.dumps("Error"))   



def eliminarComentario(request):
    if request.method =="POST":
        id = request.POST.get("id")
        try:
            com = Comentarios.objects.get(pk=id)
            com.fechaBaja = datetime.datetime.now()
            com.save()
            return HttpResponse(json.dumps("OK"))
        except Exception as e:
            return HttpResponse(json.dumps(str(e))) 


def eliminarRespuesta(request):
    if request.method =="POST":
        id = request.POST.get("id")
        try:
            respuesta = Respuestas.objects.get(pk=id)
            respuesta.fechaBaja = datetime.datetime.now()
            respuesta.save()
            return HttpResponse(json.dumps("OK"))
        except Exception as e:
            print(e)
            return HttpResponse(json.dumps("Error")) 


@login_required(login_url= '/login/')
def denunciarComentario(request,pk):
    if request.method == 'POST':
        formDenuncias   = DenunciasForm(request.POST)
        _idComentario   = pk
        comentario      = Comentarios.objects.get(id = _idComentario)
        _idUsuarioComentario = comentario.idUsuario
        _idUsuario      = request.user.id
        if formDenuncias.is_valid():
            formDenuncias                   = formDenuncias.save(commit = False)
            formDenuncias.idUsuario_id      = request.user.id 
            formDenuncias.idComentario_id   = _idComentario
            formDenuncias.fechaDenuncia     = datetime.datetime.now()
            formDenuncias.save()
            dd = Denuncias.objects.get(pk=formDenuncias.id)
            dd.idSubasta = comentario.idSubasta
            dd.save()
            controlDenunciasComentario(_idComentario)
            controlDenunciasUsuario(_idUsuarioComentario)
            return HttpResponseRedirect("/")
    else:
        formDenuncias = DenunciasForm()
    return render(request,'denunciarComentario.html', { 'formDenuncias': formDenuncias, 'idComentario': pk })


#Baja de comentarios por mas de 5 denuncias
def controlDenunciasComentario(Comentario):
    _idComentario = int(Comentario)
    cantDenunciasComentario = Denuncias.objects.filter(idComentario_id = _idComentario).count()
    if cantDenunciasComentario >= 5:
        comentario = Comentarios.objects.get(id = _idComentario)
        comentario.fechaBaja  = datetime.datetime.now()
        comentario.save()


#Baja de usuarios por mas de 20 denuncias
def controlDenunciasUsuario(_idUsuario):
    cantDenunciasUsuario    = Denuncias.objects.filter(idUsuario_id = _idUsuario).count()
    if cantDenunciasUsuario >= 20:
        usuario = User.objects.get(id = _idUsuario)
        usuario.is_active  = False
        usuario.save()


@login_required(login_url= '/login/')
def listarComentariosDenunciados(request):
    if request.method == 'GET':
        _idUsuario  = request.user.id
        #denuncias = Denuncias.objects.select_related("idComentario").filter("idComentario__fechaBaja"==None).distinct()
        denuncias = Denuncias.objects.select_related("idComentario","idMotivo").filter(idComentario__fechaBaja=None).distinct()
        listaComentariosDenunciados = []
        for d in denuncias:
            listaComentariosDenunciados.append(d)
            
        return render(request, 'listaComentariosDenunciados.html', {'listaComentariosDenunciados': listaComentariosDenunciados})

@login_required(login_url= '/login/')
def listarComentariosEliminados(request):
    if request.method == 'GET':
        _idUsuario = request.user.id
        comentarios = Comentarios.objects.all().distinct()
        listaComentariosEliminados = []

        for c in comentarios:
            if c.fechaBaja != None:
                listaComentariosEliminados.append(c)

        return render(request, 'listacomentarioseliminados.html', {'listaComentariosEliminados': listaComentariosEliminados})

def restaurarComentario(request):
    if request.method =="POST":
        id = request.POST.get("id")
        try:
            com = Comentarios.objects.get(pk=id)
            com.fechaBaja = None
            com.save()
            return HttpResponse(json.dumps("OK"))
        except Exception as e:
            return HttpResponse(json.dumps(str(e))) 


@login_required(login_url= '/login/')
def denunciarSubasta(request,pk):
    if request.method == 'POST':
        formDenuncias   = DenunciasForm(request.POST)
        _idSubasta   = pk
        subasta      = Subastas.objects.get(id = _idSubasta)
        _idUsuarioSubasta = subasta.idUsuarioVendedor
        _idUsuario      = request.user.id
        if formDenuncias.is_valid():
            formDenuncias                   = formDenuncias.save(commit = False)
            formDenuncias.idUsuario_id      = request.user.id 
            formDenuncias.idSubasta_id   = _idSubasta
            formDenuncias.fechaDenuncia     = datetime.datetime.now()
            formDenuncias.save()
            controlDenunciasSubastas(_idSubasta)
            controlDenunciasUsuario(_idUsuarioSubasta)
            return HttpResponseRedirect("/")
    else:
        formDenuncias = DenunciasForm()
    return render(request,'denunciarSubasta.html', { 'formDenuncias': formDenuncias, 'idSubasta': pk })

#Baja de comentarios por mas de 5 denuncias
def controlDenunciasSubastas(Subasta):
    _idSubasta = int(Subasta)
    cantDenunciasSubastas = Denuncias.objects.filter(idSubasta_id = _idSubasta).count()
    if cantDenunciasSubastas >= 5:
        subasta = Subastas.objects.get(id = _idSubasta)
        subasta.fechaBaja  = datetime.datetime.now()
        subasta.save()


@login_required(login_url= '/login/')
def listarSubastasDenunciadas(request):
    if request.method == 'GET':
        _idUsuario  = request.user.id
        denuncias = Denuncias.objects.select_related("idSubasta","idMotivo").filter(idSubasta__fechaBaja=None).distinct()
        listaSubastasDenunciadas = []
        
        for d in denuncias:
            listaSubastasDenunciadas.append(d)
            
        return render(request, 'listasubastasdenunciadas.html', {'listaSubastasDenunciadas': listaSubastasDenunciadas})


@login_required(login_url= '/login/')
def listarSubastasEliminadas(request):
    if request.method == 'GET':
        _idUsuario = request.user.id
        subastas = Subastas.objects.all().distinct()
        listaSubastasEliminadas = []

        for s in subastas:
            if s.fechaBaja != None:
                listaSubastasEliminadas.append(s)

        return render(request, 'listasubastaseliminadas.html', {'listaSubastasEliminadas': listaSubastasEliminadas})

@login_required(login_url= '/login/')
def restaurarSubasta(request):
    if request.method =="POST":
        id = request.POST.get("id")
        try:
            subasta = Subastas.objects.get(pk=id)
            subasta.fechaBaja = None
            subasta.save()
            return HttpResponse(json.dumps("OK"))
        except Exception as e:
            return HttpResponse(json.dumps(str(e))) 
