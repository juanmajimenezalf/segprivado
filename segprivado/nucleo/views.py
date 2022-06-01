from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from nucleo.models import Usuario
from nucleo.forms import *
from django.views.generic import CreateView, UpdateView
from django.contrib import messages
# Create your views here.


def home(request):
    medico=Usuario.objects.filter(is_medico=True)
    
    
    context={'medicos':medico,
 }
    return render(request, 'nucleo/home.html')

class medicamentoCreate(CreateView):
      model = Medicamento
      form_class = medicamentoForm
      template_name = 'nucleo/medicamentos/create.html'
      success_url = reverse_lazy('nucleo:indexMedicamento')

      def post(self, request, *args, **kwargs):
         self.object = self.get_object
         form = self.form_class(request.POST)
         if form.is_valid():
            medicamento = form.save(commit=False)
            medicamento.save()
            messages.success(request, 'Medicamento creado correctamente')
            return HttpResponseRedirect(reverse('nucleo:indexMedicamento'))
         else:
            return self.render_to_response(self.get_context_data(form=form))

class medicamentoUpdate(UpdateView):
      model = Medicamento
      form_class = medicamentoForm
      template_name = 'nucleo/medicamentos/create.html'
      success_url = reverse_lazy('nucleo:indexMedicamento')

def medicamentoDelete(request, pk):
   medicamento = get_object_or_404(Medicamento, id=pk)
   medicamento.delete()
   messages.success(request, 'Medicamento eliminado correctamente')
   return redirect('nucleo:indexMedicamento')

def medicamento(request):
   medicamentos = Medicamento.objects.all()
   context = {'medicamentos': medicamentos}
   return render(request, 'nucleo/medicamentos/index.html', context)