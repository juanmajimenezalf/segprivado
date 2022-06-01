from cProfile import label
import datetime
from faulthandler import disable
from nucleo.models import *
from django import forms

class medicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ['nombre', 'descripcion', 'receta', 'precio', 'stock']
        labels = {'nombre':'Nombre', 'descripcion':'Descripcion', 'receta':'Receta', 'precio':'Precio', 'stock':'Stock'}
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}), 
            'descripcion': forms.Textarea(attrs={'class':'form-control'}), 
            'receta': forms.TextInput(attrs={'class':'form-control'}), 
            'precio': forms.NumberInput(attrs={'class':'form-control'}), 
            'stock': forms.NumberInput(attrs={'class':'form-control'})
            }
