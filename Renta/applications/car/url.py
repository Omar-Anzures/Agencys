from django.contrib import admin
from django.urls import path

from .views import (ListCarView,
                   CarAllView,
                   PackageView,
                   DescriptionView,
                   ActiveView,
                   AutoPanelView,
                   AutoRenta,
                   AutoDetail,
                   PaquetePanelView,
                   )

app_name = "car_app"

urlpatterns = [
    path('',ListCarView.as_view(),name = 'List_car'),
    path('autos',CarAllView.as_view(),name = 'car_all'),
    path('paquetes',PackageView.as_view(),name = 'package'),
    path('descripccion/<pk>/',DescriptionView.as_view(),name = 'description'),
    path('active/',ActiveView.as_view(),name = 'active'),
    path('auto-panel/',AutoPanelView.as_view(),name = 'auto-panel'),
    path('auto-detalle/<pk>/',AutoDetail.as_view(),name = 'auto-detail'),
    path('auto-renta/',AutoRenta.as_view(),name = 'auto-renta'),
    path('paquete-panel/',PaquetePanelView.as_view(),name = 'paquete-auto'),
  
  
  
]