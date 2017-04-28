from django.shortcuts import render, render_to_response, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout as auth_logout #ver esto
from django.contrib import auth
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse


@login_required(login_url='/login/')
def productos(request):
    return render(request, "productos.html")
