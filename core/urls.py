
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, include  # add this
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("authentication.urls")),  # add this
    path("", include("app.urls"))  # add this
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

