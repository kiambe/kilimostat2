import json
import requests

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

import kilimodata
from kilimodata.models import KilimoData
from django.urls import reverse

from django.db.models import Q 
from django.views.generic import TemplateView, ListView


from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView


from .serializers import *


# from .filters import FilterKilimoDomains


def index(request):
    
    template = loader.get_template('index.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))



@api_view(['GET', 'POST'])
def data_list(request):
    if request.method == 'GET':
        req= request.GET
        data = KilimoData.objects.all()
        if 'county' not in request.GET:
            
            serializer = DataSerializer(data, context={'request': request}, many=True)

            return Response(serializer.data)

        else:
            county = request.GET["county"]
            
            county  = json.loads(county)
            
            data = data.filter(county__in=county)
            
            if 'subsector' in req:
                sector = req["subsector"]
                sector = json.loads(sector)
                print(sector)
                data = data.filter(subsector__in = sector)
            
            if 'domain' in req:
                domain = req["domain"]
                domain = json.loads(domain)
                
                data = data.filter(domain__in = domain)

            if 'elementitem' in req:
                elementitem = req["elementitem"]
                elementitem = json.loads(elementitem)
                
                data = data.filter(elementitem__in = elementitem)

            if 'uom' in req:
                uom = req["uom"]
                uom = json.loads(uom)
                
                data = data.filter(uom__in = uom)


            if 'flags' in req:
                flags = req["flags"]
                flags = json.loads(flags)
                
                data = data.filter(subdomain__in = flags)

            
            if 'domainelement' in req:
                domainelement = req["domainelement"]
                domainelement = json.loads(domainelement)
                
                data = data.filter(elements__in = domainelement)
            
            serializer = DataSerializer(data, context={'request': request}, many=True).data

            return Response(serializer)
            

    elif request.method == 'POST':
        serializer = DataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def data_detail(request, id):
    try:
        data = KilimoData.objects.get(id=id)
    except KilimoData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = DataSerializer(kilimodata, kilimodata=request.kilimodata,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class apputils(APIView):
    def get(self, request):
        
        county_data = County.objects.order_by("name")
        county_data_ser = CountySerializer(county_data, many=True).data

        subsectors_data = SubSector.objects.order_by("name")
        subsectors_ser = SectorSerializer(subsectors_data, many=True).data
        
        domains_data = Domain.objects.order_by("name")
        domain_ser = DomainSerializer(domains_data, many=True).data

        domainelements_data = DomainElement.objects.order_by("domainelement")
        domainelements_ser = DomainElementSerializer(domainelements_data, many=True).data

        elementitems_data = ElementItem.objects.order_by("name")
        elementitems_ser = ElementItemSerializer(elementitems_data, many=True).data
        
        item_category_data = ItemCategory.objects.order_by("name")
        items_category_ser = ItemCategorySerializer(item_category_data, many=True).data

        items_specify = ItemSpecify.objects.all()
        items_specify_ser = ItemSpecifySerializer(items_specify, many=True).data
        
        uoms_data = UoM.objects.order_by("name")
        uoms_ser = UoMSerializer(uoms_data, many=True).data
        
        
        
        return Response({
            "county":county_data_ser,
            "subsector":subsectors_ser,
            "domain":domain_ser,
            "domainelement":domainelements_ser,
            "elementitem":elementitems_ser,
            "items_category":items_category_ser,
            "uom":uoms_ser,            
            "items_specify":items_specify_ser
        })