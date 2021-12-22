from django.contrib import admin
from django.urls import path, re_path, include
from django.contrib.staticfiles.urls import static
from . import settings
from accounts import views
from django.views.generic import RedirectView

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('admincontrol/', admin.site.urls),
    path('', include('timeline.urls')),
    path('accounts/', include('allauth.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)