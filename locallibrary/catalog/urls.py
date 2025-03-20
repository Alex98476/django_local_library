from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  # Tento riadok bude iba cesta bez menovania
]


