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


@login_required(login_url= '/login/')
def nuevaSubasta(request):
	if request.method=='POST':
		form = SubastasForm(request.POST)
		if form.is_valid():
			nueva_subasta = form.save()
			return HttpResponseRedirect("/")	
			#return HttpResponseRedirect(reverse())
	else:
		form = SubastasForm()
	return render(request,'nuevasubasta.html', { 'form': form })


def subasta_detalle(request, pk):
        subasta = get_object_or_404(Subastas, pk=pk)
        return render(request, 'subasta_detalle.html', {'subasta': subasta})