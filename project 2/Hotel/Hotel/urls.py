from django.contrib import admin
from django.urls import path
from main.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('blog/', blog),
    path('contact/', contact),
    path('hotel/', hotel),
    path('services/', services),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
