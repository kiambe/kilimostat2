from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader


def index(request):
    
    template = loader.get_template('home/index.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))


def datadownload(request):
    
    template = loader.get_template('home/data.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))