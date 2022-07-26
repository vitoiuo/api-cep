from django.shortcuts import render, redirect
from api.models import Cep


# Create your views here.

def index(request):
    return render(request, 'consulta/index.html')


def consulta_por_cep(request):
    cep = request.GET.get('cep')

    endereco = Cep.objects.get(cep=cep)

    resposta_consulta = {
        'cep': endereco.cep,
        'logradouro': endereco.logradouro,
        'complemento': endereco.complemento,
        'bairro': endereco.bairro,
        'cidade': endereco.cidade.nome,
        'estado': endereco.cidade.estado.nome,
    }

    return render(request, 'consulta/consulta_por_cep.html', resposta_consulta)
