from datetime import date
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.views.generic import CreateView, TemplateView

from .models import RentaMode
from .forms import RentaForm


class RentaView(FormView):
    form_class = RentaForm
    template_name = 'panel/renta-auto.html'

    def form_valid(self,form):
        prestamo = RentaMode(
            perfil=form.cleaned_data['perfil'],
            autoo=form.cleaned_data['auto'],
            f_prestamo=date.today(),
           
        )
        print(prestamo)
        prestamo.save()

    

        return super(RentaView, self).form_valid(form)

