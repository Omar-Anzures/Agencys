from django.db import models

class CarModel(models.Model):
    ESTADO_CHOICES=(
        ('D','Disponible'),
        ('O','Ocupado'),
    )
    SEGMENTOS_CHOICES=(
        ('A','Chico'),
        ('B','Mediano'),
        ('C','Grande'),  
    )
    nombres = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    estado = models.CharField(max_length=1, choices=ESTADO_CHOICES, blank=True, default='D', help_text='Estado del automovil')
    tamano = models.CharField(max_length=1, choices=SEGMENTOS_CHOICES, blank=True)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='autos',blank=True,null=True)
    ratings = models.PositiveIntegerField(default = 0)


    def __str__(self):
        return self.nombres

    class Meta:
        verbose_name_plural = 'Automovil'


class CarCaratModel(models.Model):
    nombres = models.OneToOneField(
        CarModel,
        on_delete=models.CASCADE,   
        primary_key=True,
        )
    color = models.CharField(max_length=50)
    cilindros = models.IntegerField()
    puertas =  models.IntegerField()
    combustible = models.CharField(max_length=50,default=None)
    descripccion = models.CharField(max_length=250)
    transmision = models.CharField(max_length=50)

    def __str__(self):
        return self.color
    class Meta:
        verbose_name_plural = 'Caracteristica Automovil'
    


class PackageModel(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=200)
    descripccion = models.CharField(max_length=200)
    precio = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='paquetes',blank=True,null=True)
    autos = models.ForeignKey(CarCaratModel,on_delete=models.CASCADE,null=False,blank=False)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = 'Paquetes'
    

