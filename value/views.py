from django.shortcuts import render
from rest_framework import  response,status,viewsets,permissions,serializers,views,filters
from . import models as Allmodels
from .import serializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class Property_value(viewsets.ModelViewSet):
    authentication_classes=(authentication.TokenAuthentication,)
    permission_classes=(IsAuthenticated,)
    serializer_class= serializer.Propert_ValueModelserializer
    queryset=Allmodels.Propert_Value.objects.all()
class Property(viewsets.ModelViewSet):
    authentication_classes=(authentication.TokenAuthentication,)
    permission_classes=(IsAuthenticated,)
    serializer_class= serializer.PropertyModelserializer
    queryset=Allmodels.Property.objects.all()
class Expanse(viewsets.ModelViewSet):
    authentication_classes=(authentication.TokenAuthentication,)
    permission_classes=(IsAuthenticated,)
    serializer_class= serializer.ExpanseModelserializer
    queryset=Allmodels.Expense.objects.all()
class Total_NOI(viewsets.ModelViewSet):
    authentication_classes=(authentication.TokenAuthentication,)
    permission_classes=(IsAuthenticated,)
    serializer_class= serializer.NOIModelserializer  
    queryset=Allmodels.Total_NOI.objects.all() 


class authenticationClass(ObtainAuthToken):
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES