from django.db import models

from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin 

from django.db.models.signals import post_save

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

class Perfil(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='perfil')
    avatar = models.ImageField(upload_to = 'avatars', blank=True, null=True)
    edad = models.PositiveIntegerField(default=0)
    ciudad = models.CharField(max_length=50)
    direccion = models.CharField(max_length=150)
    telefono = models.CharField(max_length=10)
    cp = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.user.get_short_name()


def create_profile(sender,instance,created,**kwargs):
    if created:
        Perfil.objects.create(user=instance)
    
post_save.connect(create_profile,sender=User)