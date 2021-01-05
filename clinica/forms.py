from django import forms
from .models import Paciente, Turno
from django.forms.widgets import SelectDateWidget
from django.utils import timezone
from bootstrap_datepicker_plus import DateTimePickerInput, DatePickerInput


class PacienteCreateForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        widgets = {
            'fecha_nacimiento': DatePickerInput(),
            'telefono': forms.TextInput(attrs={'data-mask': "(+54) 000000-0000"})
        }


class TurnoListForm(forms.ModelForm):
    fecha = forms.DateField(
        required=False,
        widget=SelectDateWidget(
            years=range(timezone.now().year, timezone.now().year-10, -1), 
            empty_label=("Año","Mes","Dia"),
            attrs={'data-date-format': 'dd/mm/yyyy',
                'class': 'form-control inline-date',
                }
            ))

    def __init__(self, *args, **kwargs):
        super(TurnoListForm, self).__init__(*args, **kwargs)
        self.fields['paciente'].required = False
        self.fields['paciente'].widget.attrs.update({'class' : 'paciente-dropdown'})

    class Meta:
        model = Turno
        fields = ('fecha', 'paciente')


class TurnoCreateForm(forms.ModelForm):
    class Meta:
        model = Turno
        fields = '__all__'
        widgets = {
            'fecha': DateTimePickerInput()                  
        }
