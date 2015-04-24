from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'clinic.apps.schedule.views.index', name="index"),
]
    