from django.urls import path
from . import views

app_name = 'consulta'

urlpatterns = [
    path('', views.index, name='index'),
    path('cep/', views.consulta_por_cep, name='consulta_por_cep'),
]
