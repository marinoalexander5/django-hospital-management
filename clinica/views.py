from django.shortcuts import render, redirect
from .models import Turno, Paciente, HistorialMedico
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from .forms import PacienteCreateForm, TurnoListForm, TurnoCreateForm


# Create your views here.
def index(request):
    return render(request, 'clinica/index.html')

class TurnoListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Turno
    context_object_name = 'turnos'
    ordering = ['-fecha']

    def get_context_data(self, **kwargs):
        context = super(TurnoListView, self).get_context_data(**kwargs)
        context['form'] = TurnoListForm()
        return context

    def get_queryset(self):
        date_filter = {'year': self.request.GET.get('fecha_year'),
            'month': self.request.GET.get('fecha_month'),
            'day': self.request.GET.get('fecha_day')}
        filter_args = {}
        turnos = Turno.objects.all()
        for k, v in date_filter.items():
            if v:
                filter_args['fecha__' + k] = v
        group = self.request.user.groups.all()[0].name # Fix if multiple groups possible
        turnos = turnos.filter(**filter_args)
        if group == 'Personal Medico':
            turnos = Turno.objects.filter(profesional_medico=self.request.user)
        return turnos

    def test_func(self):
        user = self.request.user
        if user.has_perm('clinica.view_turno'):
            return True
        else :
            return False


class TurnoCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Turno
    success_url = reverse_lazy('clinica:turnos')
    form_class = TurnoCreateForm

    def test_func(self):
        user = self.request.user
        if user.has_perm('clinica.add_turno'):
            return True
        else :
            return False


class TurnoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Turno
    fields = '__all__'
    success_url = reverse_lazy('clinica:turnos')

    def test_func(self):
        user = self.request.user
        if user.has_perm('clinica.change_turno'):
            return True
        else :
            return False


class TurnoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Turno
    success_url = '/turnos/'
    
    def test_func(self):
        user = self.request.user
        if user.has_perm('clinica.delete_turno'):
            return True
        else :
            return False


class PacienteCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Paciente
    success_url = reverse_lazy('clinica:turno_create')
    form_class = PacienteCreateForm

    def test_func(self):
        user = self.request.user
        if user.has_perm('clinica.add_paciente'):
            return True
        else :
            return False


class PacienteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Paciente
    fields = '__all__'
    success_url = reverse_lazy('clinica:turno_create')

    def test_func(self):
        user = self.request.user
        if user.groups.filter(name='Secretaria').exists() or user.is_staff:
            return True
        else :
            return False


class PacienteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Paciente
    success_url = '/turnos/'
    
    def test_func(self):
        user = self.request.user
        if user.groups.filter(name='Secretaria').exists() or user.is_staff:
            return True
        else :
            return False


# class PacienteListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
#     model = Paciente
#     template_name = 'pacientes'
#     context_object_name = 'pacientes'

#     def test_func(self):
#         user = self.request.user
#         if user.groups.filter(name='Personal Medico').exists():
#             return True
#         else :
#             return False


# class HistorialMedicoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = HistorialMedico
#     success_url = "{% 'clinica:pacientes' user.id %}"

#     def test_func(self):
#         user = self.request.user
#         if user.groups.filter(name='Personal Medico').exists() or user.is_staff:
#             return True
#         else :
#             return False