from django.db import models

from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin    

from .managers import UserManager

class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=20,unique=True)
    email = models.EmailField()
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=50)
    codregistro = models.CharField(max_length=6,blank=True)
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = UserManager()

    REQUIRED_FIELDS = ['email',]

    USERNAME_FIELD = 'username'

    def get_short_name(self,):
        return self.username

    def get_full_name(self):
        return self.nombres + ' ' + self.apellidos
