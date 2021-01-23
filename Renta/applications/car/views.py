import random
from django.shortcuts import render
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView,TemplateView

from .models import CarCaratModel,PackageModel,CarModel
from applications.rentas.models import RentaMode

from django.views.generic import (
    TemplateView,
    ListView,
    DetailView
    
    )


class ListCarView(ListView):
    template_name = 'index.html'
    model = CarCaratModel
    context_object_name = "car"
    ordering = 'color'
    paginate_by = 5


class CarAllView(ListView):
    template_name = "car/car_all.html"
    model = CarCaratModel
    context_object_name = "car"
    paginate_by = 9

    def get_queryset(self):
        palabra=self.request.GET.get("kword",'')
        lista= CarCaratModel.objects.filter(
            nombres__marca__icontains=palabra
            )
        return lista 

    
class PackageView(ListView):
    template_name = 'car/paquetes.html'
    model = PackageModel
    context_object_name = "pack"
    
    
class DescriptionView(DetailView):
    template_name = 'car/descripccion.html'
    model = CarCaratModel
    context_object_name = "des"
    

class ActiveView(ListView):
    template_name = "car/activos.html"
    model = CarCaratModel
    context_object_name = "car"
    paginate_by = 9

    def get_queryset(self):
        palabra=self.request.GET.get("kword",'')
        lista= CarCaratModel.objects.filter(
            nombres__marca__icontains=palabra
            )
       # act=CarCaratModel.objects.filter(nombres__estado = 'Dispobible').filter(nombres__id = palabra)
        return lista
    
   
#Panel car

class AutoPanelView(LoginRequiredMixin,ListView):
    template_name = 'panel/auto-panel.html'
    login_url = 'users_app:login'
    model = CarCaratModel
    context_object_name = "carro"
   

    def get_queryset(self):
        barato = CarCaratModel.objects.filter(
            nombres__precio__lt = 8000
           

        )
       
        
        return barato


class Auto1PanelView(LoginRequiredMixin,ListView):
    template_name = 'car/auto1.html'
    login_url = 'users_app:login'
    model = CarCaratModel
    context_object_name = 'c1'
   
    def get_queryset(self):
        marca = CarCaratModel.objects.filter(
            nombres__marca = 'Nissan'
        )
        return marca


class Auto2PanelView(LoginRequiredMixin,ListView):
    template_name = 'car/auto2.html'
    login_url = 'users_app:login'
    model = CarCaratModel
    context_object_name = 'c2'
   
    def get_queryset(self):
        marca = CarCaratModel.objects.filter(
            nombres__marca = 'Honda'
        )
        return marca


class Auto3PanelView(LoginRequiredMixin,ListView):
    template_name = 'car/auto3.html'
    login_url = 'users_app:login'
    model = CarCaratModel
    context_object_name = 'c3'
   
    def get_queryset(self):
        marca = CarCaratModel.objects.filter(
            nombres__marca = 'Toyota'
        )
        return marca


class Auto4PanelView(LoginRequiredMixin,ListView):
    template_name = 'car/auto4.html'
    login_url = 'users_app:login'
    model = CarCaratModel
    context_object_name = 'c4'
   
    def get_queryset(self):
        marca = CarCaratModel.objects.filter(
            nombres__marca = 'Ford'
        )
        return marca


    
  
class AutoDetail(LoginRequiredMixin,DetailView):
    template_name =  'panel/auto-op.html'
    model = CarCaratModel
    context_object_name = 'op'
    login_url = 'users_app:login'



#class AutoRenta(LoginRequiredMixin,TemplateView):
 #   template_name =  'panel/renta-auto.html'
  #  login_url = 'users_app:login'


class PaquetePanelView(LoginRequiredMixin,TemplateView):
    template_name = 'panel/paquete-panel.html'
    login_url = 'users_app:login'
    