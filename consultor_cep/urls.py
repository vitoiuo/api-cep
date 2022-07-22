from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.consultar_cep, name='consultar.cep')
    # todo:
    # redirect to the app interface
]