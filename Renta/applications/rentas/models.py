from django.db import models

from applications.car.models import CarModel


class RentaMode(models.Model):
    nombres = models.CharField(max_length=30,blank=True)
    apellido = models.CharField(max_length=50,blank=True)
    email = models.EmailField(blank=True)
    ciudad = models.CharField(max_length=50,blank=True)
    estado = models.CharField(max_length=50,blank=True)
    direccion = models.CharField(max_length=150,blank=True)
    cp = models.PositiveIntegerField(default=0,blank=True)
    producto = models.ForeignKey(CarModel,on_delete=models.CASCADE,blank=True,null=True)
    stok = models.PositiveIntegerField(default=0)
    f_prestamo = models.DateField()

    def __str__(self):
        return self.nombres

    class Meta:
        verbose_name_plural = 'Renta de automoviles'



