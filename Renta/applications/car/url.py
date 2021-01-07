from django.contrib import admin
from django.urls import path

from .views import (ListCarView,
                   CarAllView,
                   PackageView,
                   DescriptionView,
                   ActiveView
                   )

app_name = "car_app"

urlpatterns = [
    path('',ListCarView.as_view(),name = 'List_car'),
    path('autos',CarAllView.as_view(),name = 'car_all'),
    path('paquetes',PackageView.as_view(),name = 'package'),
    path('descripccion/<pk>/',DescriptionView.as_view(),name = 'description'),
    path('active/',ActiveView.as_view(),name = 'active'),
  
  
]