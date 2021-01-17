from django.shortcuts import render
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView,TemplateView

from .models import CarCaratModel,PackageModel,CarModel



from django.views.generic import (
    TemplateView,
    ListView,
    DetailView
    
    )


class ListCarView(ListView):
    template_name = 'index.html'
    model = CarCaratModel
    context_object_name = "car"
    ordering = 'nombres'
    paginate_by = 4


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
    
  
class AutoDetail(LoginRequiredMixin,DetailView):
    template_name =  'panel/auto-op.html'
    model = CarCaratModel
    context_object_name = 'op'



class AutoRenta(LoginRequiredMixin,TemplateView):
    template_name =  'panel/renta-auto.html'
