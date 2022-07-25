from django.shortcuts import render
from api.models import Cep


# Create your views here.

def consulta_por_cep(request):
    context = {
        'tipo_de_consulta': 'cep'
    }
    return render(request, 'consulta/index.html', context)
