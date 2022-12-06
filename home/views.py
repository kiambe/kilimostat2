from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader




from django.db.models import Count,F,Sum,Avg
from django.db.models.functions import ExtractYear,ExtractMonth
from kilimodata.models import *
# from .utils import (
#     months,colorDanger,
#     colorPrimary,colorSuccess,
#     generate_color_palette,get_year_dict)
# Create your views here.



def index(request):
    
    template = loader.get_template('home/index.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))

def about(request):
    
    template = loader.get_template('home/about/about.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))

def faq(request):
    
    template = loader.get_template('home/about/faq.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))


def terms(request):
    
    template = loader.get_template('home/resources/terms.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))

def policy(request):
    
    template = loader.get_template('home/resources/policy.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))


def census(request):
    
    template = loader.get_template('home/resources/census.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))

def definitions(request):
    
    template = loader.get_template('home/resources/definitions.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))

def metadata(request):
    
    template = loader.get_template('home/resources/metadata.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))

def covid19(request):
    
    template = loader.get_template('home/blog/covid19.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))




def datadownload(request):
    
    template = loader.get_template('home/data.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))


