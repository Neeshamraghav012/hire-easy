
from django.contrib import admin
from django.urls import path, include
from resume.views import home
from django.conf import settings
from django.conf.urls.static import static
import accounts
import resume

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('resume.urls')),
    path('accounts/', include('accounts.urls')),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
