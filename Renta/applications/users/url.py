from django.contrib import admin
from django.urls import path

from .import views

app_name = "users_app"

urlpatterns = [
   path('registrar/',views.UserRegisterView.as_view(),name = 'registrar'),
   path('iniciar-sesion/',views.LoginView.as_view(),name = 'login'),
   path('logout/',views.LogoutView.as_view(),name='logout'),
   path('contactanos/',views.COntactView.as_view(),name = 'contact'),
   path('nosotros',views.WeView.as_view(),name = 'we'),
   path('perfil/',views.ProfileView.as_view(),name = 'profile'),
   path('update-password/',views.UpdatePasswordView.as_view(),name = 'update-p'),
   path('verificacion/<pk>/',views.VerificationView.as_view(),name = 'verification'),
   
   
   
   
   
]