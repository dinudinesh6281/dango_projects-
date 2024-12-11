from app.models import *

# Create your views here.
from rest_framework.decorators import APIView
from rest_framework.response import Response
from app.serializers import *
from rest_framework.viewsets import ViewSet,ModelViewSet

class ProductMVS(ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductModelSerializer
