from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'clinic.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'', include('clinic.apps.schedule.urls')),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
