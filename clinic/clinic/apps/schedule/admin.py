from django.contrib import admin

from .models import Doctor, Appointment


class AppointmentAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'doctor', 'date', 'time')
    ordering = ('date', 'time')


class AppointmentInline(admin.TabularInline):
    
    model = Appointment
    extra = 0
    ordering = ('date', 'time')


class DoctorAdmin(admin.ModelAdmin):

    list_display = ('name', 'specialization')
    inlines = [
        AppointmentInline,
    ]
    

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Appointment, AppointmentAdmin)
