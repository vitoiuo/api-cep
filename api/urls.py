from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('cep/<cep>', views.api_consulta_cep, name='api_consulta_cep')
]
