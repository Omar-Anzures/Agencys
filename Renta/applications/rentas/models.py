from django.db import models

from applications.users.models import Perfil
from applications.car.models import CarCaratModel


class RentaMode(models.Model):
    perfil = models.OneToOneField(Perfil,on_delete=models.CASCADE)
    autoo =  models.OneToOneField(CarCaratModel, on_delete=models.CASCADE)
    f_prestamo = models.DateField()

    def __str__(self):
        return self.autoo.nombres
