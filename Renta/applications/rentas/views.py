from datetime import date
from django.shortcuts import render

from django.urls import reverse_lazy

from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import FormView
#from django.views.generic import CreateView, TemplateView

from .forms import RentaForm
from .models import RentaMode


class RentaDetail(DetailView):
    template_name =  'panel/renta-auto.html'
    model = RentaMode

    def get_context_data(self, **kwargs): 
        context = super(RentaDetail,self).get_context_data(**kwargs) 
        print("Goaksas")
        
        context['forms'] = RentaForm
        print(context)   
        return context 


 

class RentaView(FormView):
    template_name = 'panel/renta-auto.html'
    form_class = RentaForm
    success_url = reverse_lazy('users_app:profile')
    
    
 
    def form_valid(self,form):
        prestamo = RentaMode(
       
            nombres = form.cleaned_data['nombres'],
            apellido = form.cleaned_data['apellido'],
            email = form.cleaned_data['email'],
            ciudad = form.cleaned_data['ciudad'],
            estado = form.cleaned_data['estado'],
            direccion = form.cleaned_data['direccion'],
            cp = form.cleaned_data['cp'],
            producto = form.cleaned_data['producto'],
            f_prestamo=date.today(),
           
        )
        prestamo.save()

        prestamo.stok = prestamo.stok + 1
        prestamo.save()

        
        return super(RentaView, self).form_valid(form)


    

   


    
    
   
