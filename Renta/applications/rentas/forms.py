from django import forms

from .models import RentaMode


class RentaForm(forms.ModelForm):

    f_prestamo = forms.DateField()


    class Meta:
        model = RentaMode
        fields = '__all__'

