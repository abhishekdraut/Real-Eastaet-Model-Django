from django.db.models.base import Model
from rest_framework import serializers
from .import models as Allmodels


class Propert_ValueModelserializer(serializers.ModelSerializer):
    class Meta:
        model=Allmodels.Propert_Value
        fields='__all__'

class ExpanseModelserializer(serializers.ModelSerializer):
    
    class Meta:
        model=Allmodels.Expense
        fields='__all__'
class Total_NOIModelserializer(serializers.ModelSerializer):
    class Meta:
        model=Allmodels.Total_NOI
        fields='__all__'  
class NOIModelserializer(serializers.ModelSerializer):
    value=Propert_ValueModelserializer(read_only=True,many=True)
    class Meta:
        model=Allmodels.NOI
        fields='__all__'    

class PropertyModelserializer(serializers.ModelSerializer):
    
    expanse=ExpanseModelserializer(read_only=True,many=True)
    value=Propert_ValueModelserializer(read_only=True,many=True)
    noi=NOIModelserializer(read_only=True,many=True)
    
    class Meta:
        model=Allmodels.Property
        fields='__all__'




     
