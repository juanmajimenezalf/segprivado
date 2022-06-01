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

class citaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(citaForm, self).__init__(*args, **kwargs)
        self.fields['idMedico'].queryset = Usuario.objects.filter(is_medico=True)
        
    class Meta:
        model = Cita
        fields = ['fecha', 'idMedico',]
        labels = {'fecha':'Fecha', 'idMedico':'Medico'}
        
        
        widgets = { 
            'fecha': forms.DateInput(attrs={'type':'date'}),
            
        }

    def clean_fecha(self):
        fecha = self.cleaned_data['fecha']
        if fecha < datetime.date.today():
            raise forms.ValidationError("La fecha debe ser mayor a la actual")
        return fecha

    def clean_dis(self):
        fecha = self.cleaned_data['fecha']
        idMedico = self.cleaned_data['idMedico']
        if Cita.objects.filter(fecha=fecha, idMedico=idMedico).count() > 3:
            raise forms.ValidationError("Ese medico no esta disponible en esa fecha")
        return fecha

class citaFormTratamiento(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['observaciones',]
        labels = {'observaciones':'Observaciones'}
        widgets = { 
            'observaciones': forms.Textarea(attrs={'class':'form-control'}),
            
        }