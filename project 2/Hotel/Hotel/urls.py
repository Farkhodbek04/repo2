from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('blog/', blog),
    path('contact/', contact),
    path('hotel/', hotel),
    path('services/', services),
]
