from django.contrib import admin

from .models import CarModel,CarCaratModel,PackageModel


class CarAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombres',
        'marca',
        'estado',
    )
admin.site.register(CarModel,CarAdmin)


class CarCaratAdmin(admin.ModelAdmin):
    list_display = (
        'color',
        'cilindros',
        'puertas',
        'transmision',
        'nombres'
    )
admin.site.register(CarCaratModel,CarCaratAdmin)


class PackageAdmin(admin.ModelAdmin):
    list_display = (
        'titulo',
        'subtitulo',
        'precio',
        'autos',
    )
  
admin.site.register(PackageModel,PackageAdmin)

