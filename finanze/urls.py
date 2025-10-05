# finanze/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.riepilogo_finanze, name='home'),
]