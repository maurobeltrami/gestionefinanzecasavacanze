# CasaVacanze/urls.py

from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('finanze.urls')), # La root del sito userà le URL dell'app finanze
]