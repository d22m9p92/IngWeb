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
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def listing(request):
    subasta_list = Subastas.objects.all()
    paginator = Paginator(subasta_list, 3) # Show 25 contacts per page

    page = request.GET.get('page')
    
    try:
        subastas = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        subastas = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        subastas = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {"subastas": subastas})


class home(View):
    def get(self, request): 
        subastas = Subastas.objects.all()
        categorias = Categorias.objects.all()
        '''
        paginator = Paginator(subastas, 3)

        page = request.GET.get('page')
        try:
            Subastas = paginator.page(page)
        except PageNotAnInteger:
            Subastas = paginator.page(1)
        except EmptyPage:
            Subastas = paginator.page(paginator.num_pages)        
        '''
        return render(request, "index.html",{"subastas": subastas, "categorias": categorias})

'''
def SubastaList(request):
    subastas = Subasta.objects.all()
    return render(request,"index.html",{"subastas": subastas})
'''


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