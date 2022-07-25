from django.shortcuts import render, redirect
from api.models import Cep


# Create your views here.

def index(request):
    return render(request, 'consulta/index.html')


def consulta_por_cep(request):
    cep = request.GET.get('cep')

    if cep is None or len(cep) != 8:
        return redirect('consulta_por_cep')

    endereco = Cep.objects.get(cep=cep)

    context = {
        'tipo_de_consulta': 'cep',
        'cep': endereco.cep,
        'logradouro': endereco.logradouro,
        'complemento': endereco.complemento,
        'bairro': endereco.bairro,
        'cidade': endereco.cidade.nome,
        'estado': f'{endereco.cidade.estado.nome}, {endereco.cidade.estado.sigla}',
    }

    return render(request, 'consulta/consulta_por_cep.html', context)
