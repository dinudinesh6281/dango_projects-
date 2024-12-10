from django.shortcuts import render

from app.models import *

# Create your views here.
from rest_framework.decorators import APIView
from rest_framework.response import Response
from app.serializers import *
from rest_framework.viewsets import ViewSet


class ProductCrud(ViewSet):
    def list(self,request):
        PDO=Product.objects.all()#orm
        PJO=ProductModelSerializer(PDO,many=True)#json 
        #PDO=Product.objects.get(id=id)
        #PJO=ProductModelSerializer(PDO)#json
        return Response(PJO.data)
        
    def retrive(self,request,id):
        JDO=request.data
        PDO=ProductModelSerializer(data=JDO)
        if PDO.is_valid():
            PDO.save()
            return Response({'insert':'Data is inserted Successfully'})
        else:
            return Response({'Error':'Data is not Inserted'})

    def update(self,request):
        PO=Product.objects.get(id=id)
        UPDO=ProductModelSerializer(PO,data=request.data)
        if UPDO.is_valid():
            UPDO.save()
            return Response({'update':'Data is Updated'})
        else:
            return Response({'error':'Update not done'})
    
    def partial_update(self,request):
        PO=Product.objects.get(id=id)
        UPDO=ProductModelSerializer(PO,data=request.data,partial=True)
        if UPDO.is_valid():
            UPDO.save()
            return Response({'update':'Data is Updated'})
        else:
            return Response({'error':'Update not done'})

    def destroy(self,request,id):
        Product.objects.get(id=id).delete()
        return Response({'deletion':'Data is Deleted'})
    
