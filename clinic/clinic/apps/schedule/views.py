import json
import calendar
from datetime import datetime, date
from django.shortcuts import render
from .models import Appointment, Doctor
from django.http import HttpResponseRedirect, HttpResponse
from django.forms.extras.widgets import SelectDateWidget
from django.forms.models import modelform_factory


def index(request):

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
            return HttpResponseRedirect('appointment-success/')

    doctors = Doctor.objects.all()

    context = {
        'doctors': doctors,
        'appointment_form': appointment_form,
    }

    return render(request, 'index.html', context)


def appointment_success(request):
    return render(request, 'appointment_success.html')


def get_schedule(request, doctor, date):

    if request.is_ajax():
        doctor = doctor
        weekday = (datetime.strptime(date, '%m-%d-%Y')).weekday()
        date = datetime.strptime(date, '%m-%d-%Y')

        schedule = Appointment.objects.filter(doctor=doctor, date=date)
        schedule_time = []
        for item in schedule:
            schedule_time.append(str(item.time))

        data = {}
        data['schedule_time'] = schedule_time
        data['weekday'] = weekday
        return HttpResponse(json.dumps(data), content_type='application/json')

