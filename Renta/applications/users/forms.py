from django import forms
from django.contrib.auth import authenticate
 
from .models import User


class UserRegisterForm(forms.ModelForm):
   
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input','placeholder':'Nombre de usuario'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input','placeholder':'Correo electronico'}))
    nombres = forms.CharField(widget=forms.TextInput(attrs={'class': 'input','placeholder':'Nombres'}))
    apellidos = forms.CharField(widget=forms.TextInput(attrs={'class': 'input','placeholder':'Apellidos'}))
    password1 = forms.CharField(label = 'Contraseña',required=True,widget=forms.PasswordInput(
        attrs= {
            'class':'input',
            'placeholder':'Contraseña'
            }
        )
    )
    password2 = forms.CharField(label = 'contraseña',required=True,widget=forms.PasswordInput(
        attrs= {
            'class':'input',
            'placeholder':'Repetir contraseña'
            }
        )
    )

 

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'nombres',
            'apellidos',
            
            )


    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2','Las contraseñas no son iguales')
        lista=self.cleaned_data['password1']
        if  len(lista)<= 5:
            self.add_error('password1','Ingrese una contraseña mayor a 5 digitos!')



class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': 'input',
        'placeholder':'Nombre de usuario'
        }))
    password = forms.CharField(label = 'contraseña',required=True,widget=forms.PasswordInput(
        attrs= {
            'class':'input',
            'placeholder':'Contraseña'
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm,self).clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not authenticate (username = username, password = password):
            raise forms.ValidationError("Los datos son incorrectos")

        return self.cleaned_data

class UpdateForm(forms.Form):
    password1 = forms.CharField(label = 'contraseña',required=True,widget=forms.PasswordInput(
        attrs= {
            'class':'form-control'
            
            }
        )
    )

    password2 = forms.CharField(label = 'contraseña',required=True,widget=forms.PasswordInput(
        attrs= {
            'class':'form-control'
            
            }
        )
    )

class VerificationForm(forms.Form):
    codregistro =  forms.CharField(required=True,widget=forms.PasswordInput(
        attrs= {
            'class':'input',
            'placeholder':'Ingresa el codigo de verificacion'
            }
        )
    )
    def __init__(self,pk,*args, **kwargs):
        self.id_user = pk
        super(VerificationForm,self).__init__(*args, **kwargs)


    def clean_codregistro(self):
        codigo = self.cleaned_data['codregistro']

        if len(codigo) == 6:
            activo = User.objects.cod_validation(
                self.id_user,
                codigo
            )
            if not activo:
                raise forms.ValidationError("El codigo que ingreso es incorrecto")

        else:
            raise forms.ValidationError("El codigo que ingreso es incorrecto")