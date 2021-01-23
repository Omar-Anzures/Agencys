from django import forms

from .models import RentaMode



class RentaForm(forms.ModelForm):
    nombres = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    apellido = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    ciudad = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    estado =  forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    direccion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    cp= forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))


    class Meta:
        model = RentaMode
        fields = (
            'nombres',
            'apellido',
            'email',
            'ciudad',
            'estado',
            'direccion',
            'cp',
            'producto',
         
            
            )
        widgets = {'producto':forms.Select(attrs={'class': 'form-control'})}
    
   
