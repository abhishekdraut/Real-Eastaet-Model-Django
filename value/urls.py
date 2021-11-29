from django.contrib import admin
from django.db import router
from django.urls import path,include
from . import views
from rest_framework import routers
router1=routers.DefaultRouter()
router1.register('property_value',views.Property_value,basename="Property_value")
router1.register('property',views.Property,basename="Property")
router1.register('expanse',views.Expanse,basename="Expanse")
router1.register('total_noi',views.Total_NOI,basename="Expanse")


urlpatterns = [
    
    path('',include(router1.urls)),
    path('login',views.authenticationClass.as_view(),name="authentication_class")
]