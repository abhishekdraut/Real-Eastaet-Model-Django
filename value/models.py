from django.db import models

import value

# Create your models here.
class Property(models.Model):
    Property_name=models.CharField(max_length=100 ,null=False, blank=False) 
    Avg_unit_size=models.IntegerField(null=False, blank=False)
    units=models.IntegerField(null=False, blank=False)
    Gross_rent=models.FloatField(max_length=100,null=False, blank=False)
    Cap_rate=models.FloatField(max_length=100,null=False, blank=False)
    def __str__(self):
        return self.Property_name

class NOI(models.Model):
    property=models.ForeignKey(Property,related_name='noi', on_delete=models.SET_NULL,null=True)
    Rental_income=models.FloatField(max_length=1000 ,blank=True,null=True)
    SF_month=models.FloatField(max_length=100,blank=True,null=True)
    Total_noi=models.FloatField(max_length=100,null=True, blank=True)
    def __str__(self):
        return self.property.Property_name
class Expense(models.Model):

    property=models.ForeignKey(Property,related_name='expanse', on_delete=models.SET_NULL,null=True)
    tax=models.FloatField(max_length=1000 ,blank=True,null=True)
    insurance=models.FloatField(max_length=1000 ,blank=True,null=True)
    Allowance=models.FloatField(max_length=1000 ,blank=True,null=True)
    def __str__(self):
        return self.property.Property_name

class Total_NOI(models.Model):
    property=models.ForeignKey(Property,related_name='total_noi', on_delete=models.SET_NULL,null=True)
    Tota_NOI=models.FloatField(max_length=1000 ,blank=True,null=True)
    def __str__(self):
        return self.property.Property_name

class Propert_Value(models.Model):
    property=models.ForeignKey(Property,related_name='value',on_delete=models.SET_NULL,null=True)
    Total_value=models.FloatField(max_length=1000 ,blank=True,null=True)  
    NOI_calculations=models.ForeignKey(NOI,related_name='value',on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.property.Property_name
