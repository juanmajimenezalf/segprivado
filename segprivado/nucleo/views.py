from django.shortcuts import render
from nucleo.models import Usuario
# Create your views here.


def home(request):
    medico=Usuario.objects.filter(is_medico=True)
    
    
    context={'medicos':medico,
 }
    return render(request, 'nucleo/home.html')