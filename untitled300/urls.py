from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import routing_logic

urlpatterns = [
    path('admin/', admin.site.urls),
#   path('dashboard/', include('dashboard.urls')),
    path('users/', include('users.urls')),
    path('student/', include('student.urls')),
    path('guide/', include('guide.urls')),
    path('director/', include('director.urls')),
    path('secretariat/', include('secretariat.urls')),
    path('irb/', include('irb.urls')),

    # only use this path for testing purpose
    path('project/', include('project.urls')),

    path('users/', include('django.contrib.auth.urls')),
    path('', routing_logic, name='routing_logic'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

