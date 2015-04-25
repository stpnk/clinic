from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'clinic.apps.schedule.views.index', name="index"),
    url(r'^appointment-success/', 
        'clinic.apps.schedule.views.appointment_success', 
        name="appointment_success"
    ),
    url(r'^get-schedule/(?P<doctor>\d+)/(?P<date>\d{1,2}-\d{1,2}-\d{4})/$', 
        'clinic.apps.schedule.views.get_schedule',
        name="get_schedule"
    ),

]
    