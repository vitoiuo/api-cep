from django.shortcuts import render, redirect
from api.models import Cep


# Create your views here.

def index(request):
    return render(request, 'consulta/index.html')


def consulta_por_cep(request):
    cep = request.GET.get('cep')

    endereco = Cep.objects.get(cep=cep)

    if endereco.logradouro and endereco.complemento is not None:
        resposta_consulta = {
            'cep': cep,
            'logradouro': f'{endereco.logradouro} {endereco.complemento}',
            'bairro': endereco.bairro,
            'cidade': endereco.cidade.nome,
            'estado': f'{endereco.cidade.estado.nome} ({endereco.cidade.estado.sigla})',
        }

    else:
        resposta_consulta = {
            'cep': cep,
            'logradouro': endereco.logradouro,
            'complemento': endereco.complemento,
            'bairro': endereco.bairro,
            'cidade': endereco.cidade.nome,
            'estado': f'{endereco.cidade.estado.nome} ({endereco.cidade.estado.sigla})',
        }

    return render(request, 'consulta/consulta_por_cep.html', {'resposta_consulta': resposta_consulta})
