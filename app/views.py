from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from app.models import *
from app.serializers import *

# Create your views here.


class Product_ModelViewset(ModelViewSet):
    queryset=Product.objects.all()

    serializer_class=Product_Serializer