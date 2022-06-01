from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from nucleo.models import Usuario
from nucleo.forms import *
from django.views.generic import CreateView, UpdateView, ListView
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    medico=Usuario.objects.filter(is_medico=True)
    
    
    context={'medicos':medico,
 }
    return render(request, 'nucleo/home.html')

@method_decorator(login_required, name='dispatch')
@method_decorator(staff_member_required, name='dispatch')
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

@method_decorator(login_required, name='dispatch')
@method_decorator(staff_member_required, name='dispatch')
class medicamentoUpdate(UpdateView):
      model = Medicamento
      form_class = medicamentoForm
      template_name = 'nucleo/medicamentos/create.html'
      success_url = reverse_lazy('nucleo:indexMedicamento')

@login_required
@staff_member_required
def medicamentoDelete(request, pk):
   medicamento = get_object_or_404(Medicamento, id=pk)
   medicamento.delete()
   messages.success(request, 'Medicamento eliminado correctamente')
   return redirect('nucleo:indexMedicamento')

@login_required
@staff_member_required
def medicamento(request):
   medicamentos = Medicamento.objects.all()
   context = {'medicamentos': medicamentos}
   return render(request, 'nucleo/medicamentos/index.html', context)

class medicosEspecilidad(ListView):
   model = Usuario
   template_name = 'nucleo/especialidad.html'

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      especialidadGet = self.request.GET.get('especialidad')
      
      if(self.request.GET.get('especialidad')!=0):
         data = Usuario.objects.filter(especialidad=especialidadGet, is_medico=True)
      else:
         data = Usuario.objects.filter(is_medico=True)
      
      context['data'] = data
      return context


class createCita(CreateView):
   model = Cita
   form_class = citaForm
   template_name = 'nucleo/cita/create.html'
   success_url = reverse_lazy('nucleo:home')

   def post(self, request, *args, **kwargs):
      self.object = self.get_object
      form = self.form_class(request.POST)
      if form.is_valid():
         cita = form.save(commit=False)
         cita.idPaciente = self.request.user
         cita.idMedico = form.cleaned_data['idMedico']
         cita.save()
         messages.success(request, 'Cita creada correctamente')
         return HttpResponseRedirect(reverse('nucleo:home'))
      else:
         return self.render_to_response(self.get_context_data(form=form))

def citasActual(request):
   citas = Cita.objects.filter(fecha__gte=datetime.date.today(), idMedico=request.user.id)
   context = {'citas': citas}
   return render(request, 'nucleo/cita/indexM.html', context)

class citaTratamiento(UpdateView):
   model = Cita
   form_class = citaFormTratamiento
   template_name = 'nucleo/cita/update.html'
   success_url = reverse_lazy('nucleo:actualizarCita')