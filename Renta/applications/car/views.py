from django.shortcuts import render

from .models import CarCaratModel,PackageModel

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
    
   

