from django.shortcuts import render
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail

from django.contrib.auth import authenticate,login,logout

from django.views.generic.edit import( #vamos a ocupar el FormView de enves de CreateView
    FormView
)

from django.views.generic import View,TemplateView,DetailView,ListView,UpdateView


from .models import User,Perfil #Nombre del modelo que voy a utilizar
from .functions import code_generator


from .forms import UserRegisterForm,LoginForm,UpdateForm,VerificationForm


class UserRegisterView(FormView):
    template_name = 'user/register.html'
    form_class = UserRegisterForm
    success_url = '/'

    def form_valid(self,form):
        codigo = code_generator()
        usuario = User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            nombres = form.cleaned_data['nombres'],
            apellidos = form.cleaned_data['apellidos'],
            codregistro = codigo
            
        )
        asunto='Bienvenido a nuestra comunidad Agencys!'
        mensaje = 'Codigo de verificacion: ' + codigo
        email_remitente = 'omarsatiiago@gmail.com'
        
        send_mail(asunto,mensaje,email_remitente,[form.cleaned_data['email'],])
        
        return HttpResponseRedirect(
            reverse(
                'users_app:verification',
                kwargs={'pk':usuario.id}
            )
        )



class LoginView(FormView):
    template_name = 'user/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('users_app:profile')

    def form_valid(self,form):
        user = authenticate(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password']
        )
        login(self.request,user)
        return super(LoginView,self).form_valid(form)

class LogoutView(View):
    def get(self,request,*args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'users_app:login'
            )
        )


class UpdatePasswordView(LoginRequiredMixin,FormView):
    template_name = 'panel/update-p.html'
    form_class = UpdateForm
    success_url = reverse_lazy('users_app:profile')
    login_url = reverse_lazy('users_app:profile')

    def form_valid(self,form):
        usuario = self.request.user
        user = authenticate(
            username = usuario.username,
            password = form.cleaned_data['password1']
        )
        if user:
            new_password = form.cleaned_data['password2']
            usuario.set_password(new_password)
            usuario.save()

        logout(self.request)
        return super(UpdatePasswordView,self).form_valid(form)



class VerificationView(FormView):
    template_name = 'user/verificacion.html'
    form_class = VerificationForm
    success_url = reverse_lazy('users_app:login')

    def get_form_kwargs(self):
        kwargs = super(VerificationView,self).get_form_kwargs()
        kwargs.update({
            'pk':self.kwargs['pk'],
        })
        return kwargs


    def form_valid(self,form):
        User.objects.filter(
            id = self.kwargs['pk']
        ).update(
            is_active = True
        )
        return super(VerificationView,self).form_valid(form)


class COntactView(TemplateView):
    template_name = 'user/contact.html'



class WeView(TemplateView):
    template_name = 'user/nosotros.html'


##########PANEL#################################


class ProfileView(LoginRequiredMixin,ListView):
    template_name = 'panel/profile.html'
    model = Perfil
    context_object_name = 'per'
    login_url = 'users_app:login'
    
    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        data = Perfil.objects.get(user = user.id)
        return data

