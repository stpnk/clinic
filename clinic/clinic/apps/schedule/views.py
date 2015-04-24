from datetime import date
from django.shortcuts import render
from .models import Appointment, Doctor
from django.forms.extras.widgets import SelectDateWidget
from django.forms.models import modelform_factory


def index(request):

    doctors = Doctor.objects.all()

    AppointmentForm = modelform_factory(
                            Appointment, 
                            fields=('doctor', 'name', 'date', 'time'),
                            widgets={'date': SelectDateWidget(),}
                        )

    appointment_form = AppointmentForm(initial={'date': date.today(),})

    if request.method == 'POST':
        appointment_form = AppointmentForm(request.POST)
        if appointment_form.is_valid():
            appointment_form.save()


    context = {
        'doctors': doctors,
        'appointment_form': appointment_form,
    }

    return render(request, 'index.html', context)