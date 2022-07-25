from django.urls import path
from . import views

app_name = 'consulta'

urlpatterns = [
    path('cep/<cep>', views.consulta_por_cep),
]
