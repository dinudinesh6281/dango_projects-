from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from app.models import *
from app.serializer import *
from rest_framework.permissions import IsAuthenticated


# Create your views here.

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def getuser(request):
    emps=Emp.objects.all()
    serializers=userserializer(emps,many=True)
    return Response(serializers.data)


    
    