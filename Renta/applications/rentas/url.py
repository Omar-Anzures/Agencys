from django.contrib import admin
from django.urls import path

from .import views

app_name = "rentas_app"

urlpatterns = [
     path('rentar-auto/',views.RentaDetail.as_view(),name = 'rentar'),
     path('rentar-auto/<pk>/',views.RentaView.as_view(),name = 'rentar'),
    
  
   
]